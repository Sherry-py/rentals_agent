# rentals_agent

## Project Overview
`rentals_agent` is an AI-powered smart rental assistant designed to help users find rental properties in Sydney that best match their preferences. The system automatically collects rental listings from multiple popular rental websites, filters and scores them based on customizable user criteria, and ranks the listings to optimize the online rental search experience. This project is built with remote rental processes in mind, as the user is currently not in Sydney and requires a fully online rental solution.

## Key Features
- Aggregates rental listings from popular Sydney rental platforms such as:  
  - [TenantApp](https://www.tenantapp.com.au)  
  - [Trovit Australia](https://australia.trovit.com)  
  - [Gumtree Sydney Rentals](https://www.gumtree.com.au/s-property-for-rent/rosebery-sydney/c18364l3003792)  
  - [Homely](https://www.homely.com.au)  
  - [Realestate.com.au](https://www.realestate.com.au/rent/in-rosebery,+nsw+2018/list-1)  
- Applies hard filters for essential requirements such as:  
  - Budget between AUD 700-850 per week  
  - Preferred neighborhoods including Rosebery, Kensington, Kingsford, and Randwick  
  - Move-in date from September 1, 2025, or later  
  - Mandatory features like air conditioning and well-maintained furniture  
- Implements a comprehensive multi-criteria scoring engine that evaluates listings based on price, proximity to UNSW, furniture quality, noise level, balcony presence, agent reliability, and property condition  
- Supports dynamic strategy adjustments to relax filtering criteria over time if no suitable listings are found  
- Facilitates a fully online rental search and leasing process to accommodate remote users unable to visit properties in person

## Installation & Usage
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/rentals_agent.git
  Project Structure rentals_agent/
├── README.md               # Project introduction and instructions
├── requirements.txt        # Python dependencies
├── strategy_engine.py      # Core filtering and scoring algorithm module
├── user_config.yaml        # User preferences and settings
├── listings_data/          # Collected rental listings data (JSON/CSV)
│   └── sample_listings.json
├── tests/                  # Unit tests
│   └── test_strategy.py
├── logs/                   # Runtime logs
├── scripts/                # Data collection and processing scripts
└── main.py                 # Main program entry point
Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open issues or submit pull requests to help improve the project.

⸻

Notes
	•	This project is specifically designed to address remote rental needs in Sydney, considering factors such as noise reduction, furniture quality, and proximity to UNSW
	•	The filtering and scoring logic is modular and configurable, enabling easy updates and extensions
	•	Future enhancements include integration with online communication tools and automation of rental application steps to further streamline the remote leasing process
