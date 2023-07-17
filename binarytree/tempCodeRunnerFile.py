      if current.left is not None: queue.append(current.left)
            else: queue.append(None)
            if current.right is not None: queue.append(current.right)
            else: queue.append(None)