class ClothingOrderPriorityQueue:
  """
  A priority queue for managing clothing service orders.

  Lower priority numbers mean higher urgency.
  Example:
      priority 0 = highest priority
      priority 5 = lower priority
  """

  def __init__(self):
      self.orders = []

  def is_empty(self):
      return len(self.orders) == 0

  def enqueue(self, priority, customer_name, item, completion_time):
      """
      Add a new order to the queue.
      Orders are sorted by:
      1. priority (ascending: lower number = more urgent)
      2. completion_time (descending: larger number treated as older/longer waiting)
      """
      order = {
          "priority": priority,
          "customer_name": customer_name,
          "item": item,
          "completion_time": completion_time
      }
      self.orders.append(order)
      self._sort_queue()

  def display_queue(self):
      """Print the queue in a table format."""
      if self.is_empty():
          print("The queue is empty.")
          return

      print(f"{'Priority':<10} {'Customer Name':<20} {'Item':<15} {'Completion Time':<15}")
      print("-" * 65)
      for order in self.orders:
          print(
              f"{order['priority']:<10} "
              f"{order['customer_name']:<20} "
              f"{order['item']:<15} "
              f"{order['completion_time']:<15}"
          )

  def count_by_priority(self):
      """Return a dictionary showing how many orders exist at each priority level."""
      counts = {}
      for order in self.orders:
          priority = order["priority"]
          counts[priority] = counts.get(priority, 0) + 1
      return counts

  def display_priority_counts(self):
      """Print the count of orders grouped by priority."""
      counts = self.count_by_priority()
      if not counts:
          print("No orders in the queue.")
          return

      print("Orders by priority:")
      for priority in sorted(counts):
          print(f"Priority {priority}: {counts[priority]}")

  def get_highest_priority_orders(self):
      """Return all orders with the highest priority."""
      if self.is_empty():
          return []

      highest_priority = min(order["priority"] for order in self.orders)
      return [order for order in self.orders if order["priority"] == highest_priority]

  def get_oldest_highest_priority_order(self):
      """
      Return the oldest order among the highest-priority orders.

      In this version, a larger completion_time is treated as older,
      matching the logic used in your original code.
      """
      highest_priority_orders = self.get_highest_priority_orders()
      if not highest_priority_orders:
          return None

      return max(highest_priority_orders, key=lambda order: order["completion_time"])

  def remove_oldest_highest_priority_order(self):
      """Remove and return the oldest order among the highest-priority orders."""
      order = self.get_oldest_highest_priority_order()
      if order is None:
          return None

      self.orders.remove(order)
      return order

  def upgrade_priority(self, customer_name, new_priority):
      """
      Upgrade a customer's order priority.
      Lower number = higher priority.

      Returns True if updated successfully, otherwise False.
      """
      for order in self.orders:
          if order["customer_name"].lower() == customer_name.lower():
              if new_priority < order["priority"]:
                  order["priority"] = new_priority
                  self._sort_queue()
              return True
      return False

  def remove_order(self, priority, customer_name, item, completion_time):
      """
      Remove an order matching all provided details.
      Returns True if removed, otherwise False.
      """
      for order in self.orders:
          if (
              order["priority"] == priority
              and order["customer_name"] == customer_name
              and order["item"] == item
              and order["completion_time"] == completion_time
          ):
              self.orders.remove(order)
              return True
      return False

  def normalize_priorities(self):
      """
      Reassign priorities so they become consecutive numbers
      based on current order of urgency.

      Example:
          if priorities are [0, 4, 7]
          they become [0, 1, 2]
      """
      if self.is_empty():
          return

      unique_priorities = sorted({order["priority"] for order in self.orders})
      priority_map = {old: new for new, old in enumerate(unique_priorities)}

      for order in self.orders:
          order["priority"] = priority_map[order["priority"]]

      self._sort_queue()

  def _sort_queue(self):
      """Internal helper to keep the queue sorted consistently."""
      self.orders.sort(key=lambda order: (order["priority"], -order["completion_time"]))


def print_orders(title, orders):
  """Helper function to print a list of orders."""
  print(f"\n{title}")
  if not orders:
      print("No matching orders found.")
      return

  print(f"{'Priority':<10} {'Customer Name':<20} {'Item':<15} {'Completion Time':<15}")
  print("-" * 65)
  for order in orders:
      print(
          f"{order['priority']:<10} "
          f"{order['customer_name']:<20} "
          f"{order['item']:<15} "
          f"{order['completion_time']:<15}"
      )


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
  queue = ClothingOrderPriorityQueue()

  # Add orders
  queue.enqueue(0, "Omar", "Jacket", 5)
  queue.enqueue(0, "Lily", "Shorts", 2)
  queue.enqueue(4, "Sam", "Trousers", 5)
  queue.enqueue(4, "Sandy", "Skirt", 3)
  queue.enqueue(5, "Jim", "Shorts", 2)

  print("\nInitial Queue")
  queue.display_queue()

  print("\nPriority Counts")
  queue.display_priority_counts()

  oldest_order = queue.get_oldest_highest_priority_order()
  print_orders("Oldest Highest-Priority Order", [oldest_order] if oldest_order else [])

  highest_priority_orders = queue.get_highest_priority_orders()
  print_orders("All Highest-Priority Orders", highest_priority_orders)

  removed_order = queue.remove_oldest_highest_priority_order()
  print_orders("Removed Oldest Highest-Priority Order", [removed_order] if removed_order else [])

  print("\nQueue After Removal")
  queue.display_queue()

  queue.enqueue(2, "Rana", "Hat", 1)
  print("\nQueue After Adding Rana's Order")
  queue.display_queue()

  updated = queue.upgrade_priority("Jim", 0)
  print(f"\nPriority upgrade for Jim successful: {updated}")
  queue.display_queue()

  removed = queue.remove_order(2, "Rana", "Hat", 1)
  print(f"\nRemoved Rana's order: {removed}")
  queue.display_queue()

  queue.normalize_priorities()
  print("\nQueue After Normalizing Priorities")
  queue.display_queue()