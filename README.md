# 🌾 Farmer Direct Selling

A full-stack web application that empowers farmers to sell their agricultural products **directly to consumers** — eliminating middlemen, ensuring fair pricing, and increasing farmer profits.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
- [Screenshots](#screenshots)
- [Author](#author)

---

## 📖 About the Project

**Farmer Direct Selling** is a web-based platform built during a Full Stack Development internship at **Extazee Software Solutions, Trichy**. The platform bridges the gap between rural farmers and urban consumers by providing a transparent, fair, and efficient marketplace — without any intermediaries or wholesalers.

> 🎯 **Goal:** Help farmers list their products and receive direct orders from customers, thereby increasing their profit margin.

---

## ✨ Features

### 👨‍🌾 Farmer Module
| Feature | Description |
|---|---|
| Register / Login | Secure farmer account creation and authentication |
| Add Product | List products with name, category, price, discount, and description |
| Sales Details | View incoming customer orders with delivery status |
| Update Status | Mark orders as delivered |
| Logout | Secure session termination |

### 🛒 Customer Module
| Feature | Description |
|---|---|
| Register / Login | Secure customer account creation and authentication |
| Search Products | Search available products by name |
| Purchase | View product details and place orders directly |
| My Purchases | View personal order history |
| Logout | Secure session termination |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python 3.x, Flask Framework |
| **Database** | MySQL (via PyMySQL) |
| **Database GUI** | phpMyAdmin (WAMP Server) |
| **IDE** | PyCharm Community Edition 2025.1.1 |
| **Server** | WAMP (Apache + MySQL) |

---

## 📁 Project Structure

```
FarmerSellingDirect/
│
├── main.py                  # Main Flask application & all route definitions
├── ar_master.py             # Database helper functions (select, insert, max ID)
│
├── templates/
│   ├── index.html           # Landing / Home page
│   ├── farmer.html          # Farmer login page
│   ├── farmer_home.html     # Farmer dashboard
│   ├── farmer_register.html # Farmer registration page
│   ├── farmer_add_product.html   # Add product form
│   ├── farmer_sales_details.html # View incoming orders
│   ├── farmer_status.html        # View delivered orders
│   ├── customer.html             # Customer login page
│   ├── customer_home.html        # Customer dashboard
│   ├── customer_register.html    # Customer registration page
│   ├── user_search_product.html  # Product search results
│   ├── user_search_product_1.html # Product detail page
│   ├── customer_purchase.html    # Customer order history
│   │
│   ├── css/
│   │   ├── style.css        # Custom styles
│   │   └── bootstrap.min.css
│   ├── js/
│   │   └── main.js
│   └── lib/                 # Third-party libraries (animate, owl carousel, etc.)
│
└── requirements.txt         # Python dependencies
```

---

## 🗄️ Database Schema

**Database Name:** `python_farmerdirectselling`

### Tables

#### `farmer_details`
| Column | Type | Description |
|---|---|---|
| id | VARCHAR | Primary key |
| farmer_name | VARCHAR | Full name of farmer |
| contact | VARCHAR | Phone number |
| email | VARCHAR | Email address |
| address | VARCHAR | Physical address |
| user_name | VARCHAR | Login username |
| password | VARCHAR | Login password |

#### `customer_details`
| Column | Type | Description |
|---|---|---|
| id | VARCHAR | Primary key |
| customer_name | VARCHAR | Full name of customer |
| contact | VARCHAR | Phone number |
| email | VARCHAR | Email address |
| address | VARCHAR | Delivery address |
| user_name | VARCHAR | Login username |
| password | VARCHAR | Login password |

#### `product_details`
| Column | Type | Description |
|---|---|---|
| id | VARCHAR | Primary key |
| product_name | VARCHAR | Name of the product |
| category | VARCHAR | Weight / category (e.g., 1kg) |
| price | VARCHAR | Price in ₹ |
| discount | VARCHAR | Discount percentage |
| discription | VARCHAR | Product description |

#### `sales_details`
| Column | Type | Description |
|---|---|---|
| id | VARCHAR | Primary key |
| product_name | VARCHAR | Purchased product name |
| category | VARCHAR | Product category |
| price | VARCHAR | Price at time of purchase |
| discount | VARCHAR | Discount applied |
| username | VARCHAR | Customer username |
| quantity | VARCHAR | Quantity ordered |
| total | VARCHAR | Total amount |
| delivery | VARCHAR | Status: `waiting` / `delivered` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- WAMP Server installed and running
- MySQL database created

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/FarmerDirectSelling.git
   cd FarmerDirectSelling
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install flask pymysql werkzeug
   ```

4. **Set up the database**
   - Start WAMP Server
   - Open `phpMyAdmin` → `http://localhost/phpmyadmin`
   - Create a new database: `python_farmerdirectselling`
   - Create the four tables as described in the [Database Schema](#database-schema) above

5. **Configure database connection**
   - Open `ar_master.py`
   - Update the host, username, password, and database name to match your local MySQL setup

6. **Run the application**
   ```bash
   python main.py
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:5656
   ```

---

## 📸 Screenshots

| Page | Preview |
|---|---|
| 🏠 Home Page | Organic Foods landing with Farmer & Customer buttons |
| 👨‍🌾 Farmer Dashboard | "From Our Fields To Your Family" with navigation |
| 🛒 Customer Dashboard | Product browsing interface |
| 🔍 Search Page | Search products by name with results table |
| 🔐 Login Page | Farmer / Customer login with account creation |

---

## 👤 Author

**Dhanya**
Internship Project — Full Stack Development with Python
**Extazee Software Solutions, Trichy**
📅 June 2025

---

## 📄 License

This project was developed as part of an internship program and is intended for educational purposes.

---

> *"From Our Fields To Your Family"* 🌱
