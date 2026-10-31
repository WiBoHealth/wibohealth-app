// Visitor country for the cookie banner (js/consent.js): Vercel adds x-vercel-ip-country to every request.
// Returns {"country": "NL"}, or {"country": ""} when the country is unknown. Never cached: the answer depends on the visitor.
export const config = { runtime: 'edge' };

export default function handler(request) {
    const country = (request.headers.get('x-vercel-ip-country') || '').toUpperCase();
    return new Response(JSON.stringify({ country: /^[A-Z]{2}$/.test(country) ? country : '' }), {
        headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'private, no-store' }
    });
}
