#include "lists.h"
#include <stddef.h>

/**
 * palindrome - recursive function
 * @x: pointer to a pointer to the head of singly linked list
 * @y: pointer to a listint_t node
 * Return:  1 if the list is a palindrome and 0 otherwise
 */
int palindrome(listint_t **x, listint_t *y)
{
	int output;

	if (y != NULL)
	{
		output = palindrome(x, y->next);
		if (output != 0)
		{
			output = (y->n == (*x)->n);
			*x = (*x)->next;
			return (output);
		}
		return (0);
	}
	return (1);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
