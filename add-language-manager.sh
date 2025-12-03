#!/bin/bash

# Script to add Language Manager to all HTML files
# Usage: bash add-language-manager.sh

echo "🚀 Adding Language Manager to all HTML files..."

# The line to add
SCRIPT_LINE='    <!-- Language Manager - Auto Language Switcher -->\n    <script src="/js/language-manager.js"></script>\n'

# List of files to update (Arabic - Root)
FILES=(
    "supplements.html"
    "articles.html"
    "recipes.html"
    "calculators.html"
    "about.html"
    "contact.html"
    "privacy.html"
    "terms.html"
    "disclaimer.html"
    "doctor.html"
    "pricing.html"
    "diet-plan.html"
    "calorie-tracker.html"
    "food-details.html"
)

# English files (en/)
EN_FILES=(
    "en/index.html"
    "en/foods.html"
    "en/supplements.html"
    "en/articles.html"
    "en/recipes.html"
    "en/calculators.html"
    "en/about.html"
    "en/contact.html"
    "en/privacy.html"
    "en/terms.html"
    "en/disclaimer.html"
    "en/doctor.html"
    "en/pricing.html"
    "en/diet-plan.html"
    "en/calorie-tracker.html"
    "en/food-details.html"
)

# Counter
COUNTER=0

# Process Arabic files
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        # Check if already added
        if grep -q "language-manager.js" "$file"; then
            echo "⏭️  Skipped: $file (already added)"
        else
            # Add before <style>
            sed -i "/<style>/i\\${SCRIPT_LINE}" "$file"
            echo "✅ Added to: $file"
            ((COUNTER++))
        fi
    else
        echo "❌ Not found: $file"
    fi
done

# Process English files
for file in "${EN_FILES[@]}"; do
    if [ -f "$file" ]; then
        # Check if already added
        if grep -q "language-manager.js" "$file"; then
            echo "⏭️  Skipped: $file (already added)"
        else
            # Add before <style>
            sed -i "/<style>/i\\${SCRIPT_LINE}" "$file"
            echo "✅ Added to: $file"
            ((COUNTER++))
        fi
    else
        echo "❌ Not found: $file"
    fi
done

echo ""
echo "🎉 Done! Added Language Manager to $COUNTER files!"
echo "✨ WiBo Health is now a truly bilingual website!"
