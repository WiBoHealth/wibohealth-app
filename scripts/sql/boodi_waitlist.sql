-- boodi app waitlist (wibohealth.com/boodi.html + /sv/boodi.html), 2026-11-01
-- Run once in the boodi Supabase project (Frankfurt): Dashboard -> SQL Editor -> paste -> Run.
-- The website only uses the public anon/publishable key. RLS allows INSERT only:
-- nobody can read, change or delete rows from the browser. You read the list in the dashboard
-- (Table Editor), which uses your own login, not the anon key.

create table if not exists public.waitlist (
  email      text primary key
             check (email = lower(email)
                    and length(email) <= 254
                    and email ~ '^[^@[:space:]]+@[^@[:space:]]+\.[^@[:space:]]{2,}$'),
  lang       text not null check (lang in ('ar', 'en', 'nl', 'sv')),
  consent    boolean not null check (consent = true),
  created_at timestamptz not null default now()
);

alter table public.waitlist enable row level security;

-- no access at all for browser roles, then only INSERT on the three columns the form sends
-- (created_at always comes from the database, it cannot be set from outside)
revoke all on table public.waitlist from anon, authenticated;
grant insert (email, lang, consent) on table public.waitlist to anon;

drop policy if exists "waitlist insert only" on public.waitlist;
create policy "waitlist insert only" on public.waitlist
  for insert to anon
  with check (consent = true);

-- deliberately NO select / update / delete policy.

-- Retention (privacy policy): delete within 30 days of the launch message, or 12 months after sign-up.
-- Run by hand when needed, e.g.:
--   delete from public.waitlist where created_at < now() - interval '12 months';

-- Quick check after running (as the dashboard user):
--   select count(*) from public.waitlist;
