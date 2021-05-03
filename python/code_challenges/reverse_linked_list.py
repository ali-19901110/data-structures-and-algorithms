from collections import deque
def reverse_list(ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    # put your function implementation here
    from collections import deque
    items = deque([1, 2])
    items.append(3)      
    items.rotate(1)       
    items.rotate(-1)       
    item = items.popleft() 
    return item
