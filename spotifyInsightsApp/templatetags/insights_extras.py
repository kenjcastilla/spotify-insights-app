from django import template

register = template.Library()


@register.filter
def get_indexable_item(indexable, idx):
    """
    Allows list indexing in template.
    Returns item in indexable where index = idx
    """
    return indexable[idx]


@register.filter
def get_range(val):
    """
    Returns tuple of numbers in given range.
    """
    return (num for num in range(val))
