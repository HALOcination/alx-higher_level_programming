#include "lists.h"

/**
* reverse_listint - reverses a linked list
* @head: arg
* BY: HALO
*
* Return: first node indic in the new list
*/

void reverse_listint(listint_t **head)
{
  listint_t *previous = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = previous;
      previous = current;
      current = next;
    }

  *head = previous;
}

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: arg
* BY: HALO 
*
* Return: 1 if it is a palindrom, 0 if not
*/

int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *tmp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = slow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = slow->next->next;
	  break;
	}
      slow = slow->next;
    }

  reverse_listint(&dup);

  while (dup && tmp)
    {
      if (tmp->n == dup->n)
	{
	  dup = dup->next;
	  tmp = tmp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}
