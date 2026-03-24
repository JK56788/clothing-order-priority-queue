# Clothing Order Priority Queue

A Python-based priority queue system for managing clothing service orders such as laundry, tailoring, or repairs.

## Overview

This project implements a priority queue to organize customer orders based on urgency and completion time. It simulates how a clothing service business might manage incoming tasks efficiently.

Orders are processed based on:
1. **Priority level** (lower number = higher urgency)
2. **Completion time** (used to determine oldest orders)

---

## Features

- Add new orders to the queue
- View all orders in a structured format
- Count orders by priority level
- Retrieve all highest-priority orders
- Identify and remove the oldest highest-priority order
- Upgrade a customer’s priority
- Remove a specific order
- Normalize priority levels for consistency

---

## Data Structure

Each order contains:
- `priority` → urgency level (lower = more urgent)
- `customer_name` → name of the customer
- `item` → clothing item (e.g. jacket, trousers)
- `completion_time` → numeric value representing time

The queue is internally sorted using:
- priority (ascending)
- completion_time (descending)

---

## Example Usage

```python
queue = ClothingOrderPriorityQueue()

queue.enqueue(0, "Omar", "Jacket", 5)
queue.enqueue(4, "Sam", "Trousers", 5)

queue.display_queue()

```

---

## Why This Project

This project was built to demonstrate understanding of:

- Object-Oriented Programming (OOP)
- Custom data structures using Python lists
- Sorting with multiple conditions
- Searching, updating, and deleting records
- Writing cleaner and more maintainable code

---

## Possible Improvements

- Save/load queue data from a file
- Replace completion time with real timestamps
- Add a graphical user interface (GUI)
- Implement a heap-based priority queue for better performance
- Add unit tests

---

## How to Run

```bash
python clothing_order_priority_queue.py
```

---

## Author

Joseph Egbejule
