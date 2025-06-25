#include<stdio.h>
#include<stdlib.h>
#include <string.h>


/*
 Linkedlist -> A linked list is a linear data structure where elements are not stored in contiguous memory locations 
 like arrays. Instead, each element (node) contains data and a reference (pointer) to the next node in the sequence. 
 This structure allows for efficient insertion and deletion of elements compared to arrays, 
 as it doesn't require shifting elements after modification. 

*/

struct Node {
    int data; // store the value (int)
    struct Node* next; // Pointer to the next Node
};


struct Linkedlist {
    struct Node* head; // Pointer to the first node
    int size; // Tracks the number of nodes
};

void initLinkedlist(struct Linkedlist* list) {
    list-> head = NULL; // no Nodes yet
    list-> size = 0; // init size of LinkedList 0
}


void insertAtBegining(struct Linkedlist* list, int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node)); // Allocate Memory for a new node
    newNode-> data = data; // Added a value 
    newNode-> next = list-> head; // New node points to old head
    list-> head = newNode; // Head now points to new node
    list-> size++;
}


void deleteBeginning(struct Linkedlist* list) {
    if (list->head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return;
    }
    
    struct Node* temp = list->head;      // Store the current head
    list->head = list->head->next;       // Move head to the next node
    free(temp);                          // Free the old head
    list->size--;                        // Decrement size
}

void printList(struct Linkedlist* list) {
    struct Node* current = list->head; // start from Head
    printf("Linked List: ");
    while (current != NULL) { // Loop until last Node (NULL)
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
    printf("Size: %d\n", list->size);
}

int main(){
    struct Linkedlist list;
    initLinkedlist(&list); // Intialize empty list
    
    for(int i = 1; i <= 10; i++){
        insertAtBegining(&list, i); // List: 10 -> 9 -> ... -> 1 -> NULL
    }
    deleteBeginning(&list); //List: removes(10) List: 9 -> ... -> 1 -> NULL
    printList(&list); // output: 9 -> ... -> 1 -> NULL
    
    return 0;

}
