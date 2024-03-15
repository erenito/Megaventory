# Inventory Management API

## Overview
This project consists of a RESTful API developed with Flask, designed for inventory management operations. It interfaces with an external inventory management service (Megaventory) to perform CRUD operations related to products, clients/suppliers, and inventory locations. The API serves as a backend system, enabling seamless interaction with the Megaventory API by abstracting request and response handling through a simplified interface.

## Files and Structure
- **app.py**: The main Flask application file. It defines endpoints for inserting and retrieving products, clients/suppliers, inventory locations, and managing relations among them.
- **models.py**: Contains class definitions for `Product`, `SupplierClient`, and `InventoryLocation`. Each class provides a `to_json` method, facilitating the conversion of object instances to a JSON format suitable for API requests.

## Key Features
- **Product Management**: Insert new products and retrieve existing ones by SKU.
- **Client/Supplier Management**: Insert and retrieve clients or suppliers, distinguishing them by type.
- **Inventory Location Management**: Insert new inventory locations and retrieve existing ones by abbreviation.
- **Relationship Management**: Establish and manage relationships between products and clients/suppliers, products and inventory locations.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework used to create the API endpoints.
- **Requests**: A simple HTTP library used to make requests to the Megaventory API.


## Connection to SUpotify Project
This inventory management API project underpins the development skills and understanding of RESTful API concepts that were critical in the SUpotify project. Although SUpotify is a music recommendation application and fundamentally different in purpose, the underlying principles of interfacing with external APIs, managing data transactions, and handling client-server interactions are consistent across both projects. My work on this inventory management API reinforced my capabilities in back-end development, database management, and the integration of third-party services—skills that were pivotal in the successful implementation of SUpotify's server-side functionality and its interaction with Spotify and Genius APIs for music data.
