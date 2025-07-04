🏠 rentals_agent

🚀 A practical, learning-oriented project to practice Python end-to-end development while helping find a suitable apartment in Sydney for September move-in.

⸻

🎯 Project Purpose

✅ Skill Development:
	•	Practice scraping (requests, Playwright), pandas data handling, visualization (matplotlib/plotly), and project structuring in PyCharm + Trae.
	•	Build the habit of independent vibe coding with real-life projects.

✅ Practical Goal:
	•	Actively assist in renting an apartment in Sydney, ensuring data-driven price comparison and effective decision-making while maintaining flexibility.

⸻

🚩 Project Strategy

After encountering API and anti-scraping limitations on major platforms, we refined our approach:

✅ Targeted, low-frequency scraping of 5–8 key suburbs only (Kingsford, Kensington, Randwick, Waterloo, Zetland, Rosebery, etc.).
✅ Combine manual collection (Facebook Marketplace, WeChat groups) for accurate, up-to-date listings.
✅ Store and manage listings in Airtable/Notion for easy tracking and comparison.
✅ Weekly routine: scrape → update database → analyze → schedule inspections.

This ensures the project maximizes both learning value and practical effectiveness in finding a rental property.

⸻

🗓️ Project Progress Structure

To maintain focus and consistency:

Day 1:
	•	Identify target suburbs + price ranges.
	•	Create Airtable/Notion database structure.
	•	Set up Playwright scraping environment and test grabbing top 5 listings.
	•	Generate demo suburb price distribution plot.

Day 2:
	•	Refine scraping fields (title, price, address, bedrooms, link) and storage pipeline.
	•	Improve visualization clarity.
	•	Push initial functional version to GitHub.

Day 3:
	•	Supplement data with Facebook/WeChat manual collection.
	•	Validate data accuracy by comparing with live platforms.
	•	Create simple scoring logic for properties.

Day 4:
	•	Generate comparative graphs and average price tables.
	•	Prepare automated email inquiry templates with ChatGPT.
	•	Plan weekend inspection scheduling.

Day 5:
	•	Send out initial inquiries and track response status.
	•	Run complete scraping pipeline, validating stability.

Day 6:
	•	Add error handling and logging for scraping failures.
	•	Experiment with Airtable API auto-sync.
	•	Output weekly scrape summary visuals.

Day 7:
	•	Conduct or schedule viewings.
	•	Compare options for time, location, and price.
	•	Document weekly progress and plan next iterations.

⸻

📊 Features Planned

✅ Playwright-based targeted scraping of Sydney rental listings (top 5 per suburb).
✅ Data cleaning and pandas-based structuring.
✅ Price distribution visualization for key suburbs.
✅ Airtable/Notion management for rental pipeline.
✅ Weekly inspection planning support.
✅ ChatGPT-assisted inquiry and negotiation template generation.

⸻

🌿 Future Extensions
	•	Adapt this pipeline for supermarket price monitoring, flight/visa booking monitoring, or application tracking.
	•	Integrate with Telegram/Discord bot for push notifications.
	•	Expand into an AI-assisted rental agent system