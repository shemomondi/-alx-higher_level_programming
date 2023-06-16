#include <stddef.h>
#include "lists.h"

size_t dlistint_len(const dlistint_t *h)
{
    size_t length = 0;

    while (h != NULL)
    {
        length++;
        h = h->next;
    }

    return length;
}

