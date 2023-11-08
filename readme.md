# Course Selling Website

[![GitHub Repository](https://img.shields.io/badge/GitHub%20Repo-Course%20Selling%20Website-green)](https://github.com/rajatrawal/video-course)
[![Render Live Demo](https://img.shields.io/badge/Render-Live%20Demo-brightgreen)](https://video-course.onrender.com/)
[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Web%20Framework-blue)](https://www.djangoproject.com/)
[![Razorpay](https://img.shields.io/badge/Razorpay-Payment%20Gateway-blue)](https://razorpay.com/)
[![YouTube](https://img.shields.io/badge/YouTube-Video%20Integration-blue)](https://www.youtube.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-blue)](https://www.sqlite.org/)

📚 Welcome to the "Course Selling Website" project! This platform allows users to browse and purchase courses created by administrators. It's integrated with Razorpay for seamless payments, and course content is hosted privately on YouTube. Users can also apply coupon codes to avail discounts. The admin page login credentials are "admin" for both the username and password. The project is deployed on Render for convenient access.

## About This Project

The "Course Selling Website" is designed for users who want to buy courses on a variety of subjects. Key features include:

1. **Course Listings**: Browse and view available courses.

2. **Secure Payments**: Integrated with Razorpay for secure payment processing.

3. **Private YouTube Videos**: Courses are hosted privately on YouTube for easy access.

4. **Coupon Codes**: Users can apply coupon codes to get discounts.

5. **Admin Panel**: Admins can manage courses and user orders.

## Preview

![image](https://github.com/rajatrawal/video-course/assets/72153827/b231e077-fd9c-4ecb-8233-c059f7f58cfb)

## Usage

1. Explore the live demo of the "Course Selling Website" [here](https://video-course.onrender.com/).

2. Browse available courses and choose the one you want to purchase.

3. Complete the payment using the secure Razorpay payment gateway.

4. Access course content via private YouTube videos.

## Installation

To run this project locally for development purposes, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/rajatrawal/video-course.git
   ```

2. Navigate to the project directory:

   ```shell
   cd video-course
   ```

3. Create a `.env` file in the project's root directory and store the following secret variables:
   
   ```shell
   KEY_SECRET = "your_razorpay_secret_key"
   KEY_ID = "your_razorpay_key_id"
   ```

4. Update the Razorpay key in the `checkout.html` script tag. Open the `checkout.html` file and find the following script tag:

   ```html
   <script>
       var options = {
           "key": "your_razorpay_key_id",
           // ... other options
       };
   </script>
   ```

   Replace `"your_razorpay_key_id"` with your actual Razorpay key ID.

5. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

7. Start the development server:

   ```shell
   python manage.py runserver
   ```

8. Open your web browser and explore the project locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Admin Panel

Access the admin panel to manage courses and user orders. Use the following login credentials:

- **Username**: admin
- **Password**: admin


## Contribute

If you'd like to contribute to this project, have suggestions for improvement, or wish to add more features, please feel free to submit issues or pull requests on [GitHub](https://github.com/rajatrawal/video-course). Your contributions are greatly appreciated! 🚀

Thank you for exploring the "Course Selling Website" project. We hope it provides a seamless course purchasing experience for your users. 📖
