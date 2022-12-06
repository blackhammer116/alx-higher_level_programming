#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to the head of the list
 * Return: 1 if its palindrome, else 0
 */

int is_palindrome(listint_t **head)
{
        if (*head == NULL)
        {
                return (1);
        }

        listint_t *current, *prev = NULL, *nxt = NULL, *temp = *head;
        current = *head; 
          
        while (current)        {
                nxt = current->next;
                current->next = prev; 
                prev = current;
                current = nxt;
        }    
        current = prev;

        while (temp)
        {
                if (temp->n == current->n)
                {
                        temp = temp->next; 
                        current = current->next;
                }
                else
                        return (0);
        } 
		return (1);

}
