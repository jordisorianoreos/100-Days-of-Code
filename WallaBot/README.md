# 🛍️ WallaBot - Wallapop Scraper and Notification Bot

**WallaBot** is a Python-based web scraping bot designed to track product listings on Wallapop, a popular Spanish online marketplace for second-hand goods. The bot monitors specific product searches, scrapes details about available items, and sends notifications when new listings are found. All scraped data is stored in an Excel file for easy tracking and market analysis.

## ✨ Features

### 🛒 Product Scraping
- The bot scrapes products such as **Kindles** from Wallapop, retrieving the following details:
  - **Title**
  - **Price**
  - **Link to product**
- The data is stored in an **Excel file** for easy access and analysis.
- A dedicated sheet is created for each search URL, with a summary sheet for all products found.

### 🚨 Notifications
- **Push Notifications**: The bot sends desktop notifications when a new product is found.
- **Email Notifications**: The bot can send product details via email to a specified address.

### 🌍 Location-Based Search
- The bot randomizes the geographical coordinates (latitude and longitude) in the search URLs to simulate browsing from different locations.
- This helps ensure more accurate and varied product listings.

### 📝 Excel Output
- The bot stores the scraped data in an Excel file (`productos_encontrados.xlsx`), organized by product URL.
- The Excel sheet includes **hyperlinks** to each product listing for easy navigation.

## 🛠️ Technologies Used

- **Selenium**: For web scraping and automating browser actions.
- **Pandas**: For data manipulation and storing results in Excel format.
- **plyer**: For desktop push notifications.
- **smtplib**: For sending email notifications.
- **Python-dotenv**: For managing environment variables (like email credentials and API keys).
- **OpenPyXL**: For writing data to Excel files.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory:
   ```bash
   cd "WallaBot"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up `.env` file:
   ```bash
   MY_EMAIL=your-email@example.com
   MY_PASSWORD=your-email-password
   ENDPOINT_EMAIL=recipient-email@example.com
   ACCOUNT_SID=your-twilio-account-sid
   AUTH_TOKEN=your-twilio-auth-token

4. Run the bot:
   ```bash
   python main.py
   ```

5. Output
- The bot will scrape data from the specified Wallapop URLs.
- Notifications will be sent whenever a new product is found.
- The data will be stored in `productos_encontrados.xlsx`.

## 📈 Customizing the Bot
- **Add More Search URLs**: You can add more product search URLs to the `products_urls` list.
- **Customize Product Keywords**: Change the `keywords` parameter in the search URL to track different items (e.g., `iphone`, `laptop`, etc.).
- **Notification Settings**: Modify email and push notification settings as per your preference.

## 📝 Future Improvements
- **Captcha Bypass**: Implement methods to handle or bypass captchas on Wallapop.
- **Advanced Product Filtering**: Add more advanced filtering options for scraping specific types of products.
- **Frequency Control**: Schedule the bot to run at regular intervals, such as once per day or hour.

## 📧 Contact

If you have any questions, comments, or simply want to connect, feel free to reach out:

- **Email**: [jordisorianoreos@gmail.com](mailto:jordisorianoreos@gmail.com)
- **LinkedIn**: [Jordi Soriano Reos](https://www.linkedin.com/in/jordi-soriano-reos/)

Thank you for visiting my repository!
