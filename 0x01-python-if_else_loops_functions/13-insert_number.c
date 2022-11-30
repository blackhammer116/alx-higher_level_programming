#include "lists.h"
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: head pointer to a list
 * @number: number to be inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if ((temp->n) >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while(temp)
	{
		if (!(temp->next))
		{
			if ((temp->n) <= number)
			{
				temp->next = new;
				return (new);
			}
		}
		if ((temp->next->n) >= number)
		{
			new->next = temp->next;
			temp->next = new;
			break;
		}
		temp = temp->next;
	}
	return (new);
}
