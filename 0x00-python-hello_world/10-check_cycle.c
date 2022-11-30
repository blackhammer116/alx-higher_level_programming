#include "list.h"
/**
 * check_cycle - checks a cycle within a linked list
 * @list: list pointer
 * Return: 0 if no cycle found, 1 if their is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prv = list;
	listint_t *nxt = list;

	if (!list)
		return (0);

	while (prv && nxt && nxt->next)
	{
		prv = prv->next;
		nxt = nxt->next->next;
		if (prv == nxt)
			return (1);
	}
	return (0);
}
