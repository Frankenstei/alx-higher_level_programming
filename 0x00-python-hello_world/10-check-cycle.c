/*
 * File: 10-check_cycle.c
 * Auth: Brennan D Baraban
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *start, *end;

	if (list == NULL || list->next == NULL)
		return (0);

	start = list->next;
	end = list->next->next;

	while (start && end && end->next)
	{
		if (start == end)
			return (1);

		start = start->next;
		end = end->next->next;
	}

	return (0);
}
