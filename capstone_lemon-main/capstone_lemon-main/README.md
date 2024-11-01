# Little Lemon Restaurant API Documentation

## Overview
Welcome to the Little Lemon Restaurant API! This API allows you to manage the restaurant’s menu items, handle customer bookings, and utilize token-based authentication.

---

### Menu Endpoints

- **`GET /restaurant/menu/`**  
  Retrieve the list of all menu items.

- **`POST /restaurant/menu/`**  
  Add a new item to the restaurant's menu.

- **`GET /restaurant/menu/<int:item_id>`**  
  Fetch details for a specific menu item, identified by `item_id`.

- **`PUT /restaurant/menu/<int:item_id>`**  
  Update details of a specific menu item, identified by `item_id`.

- **`DELETE /restaurant/menu/<int:item_id>`**  
  Remove a menu item from the list using its unique `item_id`.

---

### Booking Endpoints

- **`GET /restaurant/booking/`**  
  Retrieve a list of all existing bookings.

- **`POST /restaurant/booking/`**  
  Create a new booking for a customer.

- **`GET /restaurant/booking/<int:booking_id>`**  
  Fetch details for a specific booking, identified by `booking_id`.

- **`PUT /restaurant/booking/<int:booking_id>`**  
  Update an existing booking, identified by `booking_id`.

- **`DELETE /restaurant/booking/<int:booking_id>`**  
  Cancel a booking using its unique `booking_id`.

---

### Authentication Endpoint

- **`POST /api-token-auth/`**  
  Obtain an authentication token required for accessing protected routes. 

---

This API structure provides comprehensive access to menu and booking management for the Little Lemon Restaurant.