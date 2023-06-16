#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    dlistint_t *head;
    dlistint_t *new;
    dlistint_t hello = {8, NULL, NULL};
    size_t n;

    head = &hello;
    new = malloc(sizeof(dlistint_t));
    if (new == NULL)
    {
        fprintf(stderr, "Error: Can't malloc\n");
        return EXIT_FAILURE;
    }
    new->n = 9;
    new->prev = NULL;
    new->next = head;
    head->prev = new;
    head = new;

    n = dlistint_len(head);
    printf("-> %lu elements\n", n);

    free(new);
    return EXIT_SUCCESS;
}

