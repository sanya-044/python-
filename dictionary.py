{
 "cells": [
  {
   "cell_type": "raw",
   "id": "8f5ac3a6-ab69-4aa6-9eee-19a15309dac6",
   "metadata": {},
   "source": [
    "#notesssss.....\n",
    "#syntax of dict \n",
    "#dict_name={key:value}\n",
    "#phone_no={'ram':1234, 'shyam':456 , 'mohan': 8900}\n",
    "\n",
    "if suppose i want to find acccess the roll no. ram..i can get it using keys\n",
    "\n",
    "values are mutable but the keys should be immutable..no duplicates allowed\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3424a58a-ed15-4de3-8172-e385c3390203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ram': 1234, 'shyam': 456, 'mohan': 8900}\n"
     ]
    }
   ],
   "source": [
    "#if we want to access dictionary\n",
    "\n",
    "phone_no={\n",
    "          'ram':1234,    \n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "print(phone_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4e876220-074a-41e1-a1b7-e4899bdfc8ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "456\n"
     ]
    }
   ],
   "source": [
    "#if we want to acess phone no. of particular person \n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "print(phone_no['shyam'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "63c80389-8c60-4251-a36f-53331807492e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'ram': 1111, 'shyam': 456, 'mohan': 8900}"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#what if duplicates ARE there?\n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan':8900,\n",
    "          'ram':1111\n",
    "         }\n",
    "phone_no"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f79f7d9b-ce11-457c-8e3c-04abdcb72c50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ram': 1234, 'shyam': 456, 'mohan': 8900}\n"
     ]
    }
   ],
   "source": [
    "#another method to create dictionary\n",
    "phone_no=dict({\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         })\n",
    "print(phone_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "052e1631-c962-460a-8b9b-057ab3611d77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ram': 1234, 'shyam': 3456, 'mohan': 8979}\n",
      "{'ram': 1234, 'shyam': 3456, 'mohan': 9999}\n"
     ]
    }
   ],
   "source": [
    "#another method to create dictionary and update its data\n",
    "phone_no=dict([('ram',1234),('shyam',3456),('mohan',8979)])\n",
    "print(phone_no)\n",
    "phone_no['mohan']=9999 #UPDATING THE VAL OF MOHAN\n",
    "print(phone_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e065ee25-3529-4037-9e06-00fa204528d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ram': 1234, 'shyam': 456, 'mohan': 8900}\n",
      "{'ram': 1234, 'shyam': {'shyam_home': 5555, 'shyam_work': 666}, 'mohan': 8900, 'madann': {444, 333, 111}}\n",
      "{'shyam_home': 5555, 'shyam_work': 666}\n",
      "666\n",
      "1234\n"
     ]
    }
   ],
   "source": [
    "#adding more items to dictionary\n",
    "\n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "print(phone_no)\n",
    "phone_no['madann']={111,333,444}\n",
    "phone_no['shyam']={'shyam_home':5555,'shyam_work':666}\n",
    "print(phone_no)\n",
    "#if we want to access the phone no. of shyam\n",
    "print(phone_no['shyam'])\n",
    "print(phone_no['shyam']['shyam_work'])\n",
    "\n",
    "#using get method also we can access\n",
    "print(phone_no.get('ram'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c8b441ad-d294-4f26-a945-a6e7a8bf5911",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hmm\n"
     ]
    }
   ],
   "source": [
    "data={\n",
    "    1:'hi',\n",
    "    2:'km',\n",
    "    0:'hmm'\n",
    "}\n",
    "print(data[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6fabb121-b2cb-42cc-879d-ff95026296a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'shyam': 456, 'mohan': 8900}\n"
     ]
    }
   ],
   "source": [
    "#deleting any item from dict\n",
    "\n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "del phone_no['ram']\n",
    "print(phone_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9c8c6140-0eba-408a-a538-c50a05382c47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('mohan', 8900)\n",
      "{'ram': 1234, 'shyam': 456}\n"
     ]
    }
   ],
   "source": [
    "#deleting using pop\n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456,\n",
    "          'mohan':8900,\n",
    "         }\n",
    "#phone_no.pop('mohan') \n",
    "print(phone_no.popitem()) #deletes last  item and returns the deleted key value pair\n",
    "print(phone_no)\n",
    "\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "27d6d6d4-2ca6-42fd-893a-ab2244c8c693",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "#deleting all items from dictionary\n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "phone_no.clear()\n",
    "print(phone_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "240fc28a-7df1-405b-9a4b-19e9978c1457",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['ram', 'shyam', 'mohan'])\n",
      "dict_values([1234, 456, 8900])\n",
      "dict_items([('ram', 1234), ('shyam', 456), ('mohan', 8900)])\n"
     ]
    }
   ],
   "source": [
    "#accessing only keys or values\n",
    "\n",
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "print(phone_no.keys())\n",
    "print(phone_no.values())\n",
    "print(phone_no.items()) #returns list of all items but in the form of tupple i.e it returns a list of tupple pairs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "aad65883-b179-432d-9ff8-dcc199795efd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram\n",
      "shyam\n",
      "mohan\n"
     ]
    }
   ],
   "source": [
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "} \n",
    "for i in phone_no:\n",
    "    print(i)          #this only returns keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0b698513-61c3-459d-9107-5c9d33cfd04f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram\n",
      "1234\n",
      "shyam\n",
      "456\n",
      "mohan\n",
      "8900\n"
     ]
    }
   ],
   "source": [
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "}\n",
    "for i in phone_no:\n",
    "    print(i)\n",
    "    print(phone_no[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8869432a-22b3-4085-a56d-361a9568062f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('ram', 1234)\n",
      "('shyam', 456)\n",
      "('mohan', 8900)\n"
     ]
    }
   ],
   "source": [
    "phone_no={\n",
    "          'ram':1234,\n",
    "          'shyam':456 ,\n",
    "          'mohan': 8900\n",
    "         }\n",
    "for i in phone_no.items():\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcca2f3c-4327-485e-b41f-6d7548909160",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
