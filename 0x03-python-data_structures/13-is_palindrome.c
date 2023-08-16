#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindromme - check if the linked list is palindrome
 * @head: linked list to be checked
 * Return: 0 if not palindrome, otherwise 1
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = *head;
	listint_t *midnode = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
	/* Find the middle of the list */
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

	/* If the list has odd number of elements, skip the middle node */
		if (fast != NULL)
		{
		midnode = slow;
		slow = slow->next;
		}

	/* Reverse the second half of the list */
		second_half = slow;
		prev_slow->next = NULL;
		reverse_list(&second_half);

	/* Compare the first and second halves for palindromicity */
		is_palindrome = compare_lists(*head, second_half);

	/* Reconstruct the original list */
		reverse_list(&second_half);
		if (midnode != NULL)
		{
			prev_slow->next = midnode;
			midnode->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}

	return (is_palindrome);
}

/**
 * reverse_list - reverse a given linked list
 * @head: list to be reversed
 *
 * Return: Nothing
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_list - compare two given list
 *
 * @list1: the first list to be compared with
 * @list2: the second list
 *
 * Return: 1 if they are palindrome, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->data != list2->data)
		{
			return (0);
		}
		list1 = list1->next;
		list2 = list2->next;
	}

	/* If both lists are exhausted, they are palindromic */
	if (list1 == NULL && list2 == NULL)
	{
		return (1);
	}

	/* If one list is exhausted while the other is not, not palindromic */
	return (0);
}

