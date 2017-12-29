#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

/*
1. find and remove matched element from linked list.
2. from head to end of the Linkedlist, keep search for matched element,
   * if an element if matched, link privious element to matched element noxt node and free the matched element.
   * if element is no matched dont take any action.
   * move the pointer to next element.
   * continue this step until node is NULL.


*/

struct element{
    int data;
    struct element * ptr;

};

typedef struct element * NODE;

void PrintElements(NODE Head){
    NODE temp = Head;
    int count = 0;
    while(temp != NULL){
        printf("element at pos: %d is %d \n", count, temp->data);
        count ++;
        temp = temp->ptr;
    }
}

NODE PushElement(NODE Head, int value){
    NODE temp = Head;
    if (Head == NULL){
        NODE new = malloc(sizeof(struct element));
        new->data = value;
        new->ptr = NULL;
        return new;
    }
    while(temp->ptr != NULL){
        temp = temp->ptr;
    }
    NODE new = malloc(sizeof(struct element));
    new->data = value;
    new->ptr = NULL;
    temp->ptr = new;
    return Head;
}

NODE StoreElements(NODE Head, int size){
    int value, i;
    printf("Enter elements to be stored in array \n");
    for (i = 0; i< size; i++ ){
        scanf("%d", &value);
        Head = PushElement(Head, value);
    }
    return Head;
}

NODE RemoveMatchedInstance(NODE Head, int match){
    NODE temp = NULL;
    NODE move = NULL;
    NODE prev = NULL;

    if(Head == NULL){
        return NULL;
    }
    else if(Head->data == match && Head->ptr == NULL){
	free(Head);
	return NULL;
	}
 
    move = Head;
    prev = NULL;

    bool is_head = false;
    while(move != NULL){
        temp = NULL;
        if (move->data == match){
            temp = move;
            if(prev != NULL)
            {
	            prev->ptr = move->ptr;
        	    move = prev;
	   }
	    else{                           // if first element itself is matched, move head element
			Head = Head->ptr;
                        is_head = true;
		}
        }
        if (!is_head )   //if head is removed, keep previous as NULL
            prev = move;

        move = move->ptr;
        if(!temp) free(temp);
    }
    return Head;

}

int main(){
    int size, match;

    printf("Enter Linked list size \n");
    scanf("%d", &size);
    
    NODE Head = NULL;
    Head = StoreElements(Head, size);

    printf("Enter data to be matched \n");
    scanf("%d", &match);
    fflush(stdin);

    Head = RemoveMatchedInstance(Head, match);
    printf("Elements after removing matched elements \n");
    PrintElements(Head);

}
