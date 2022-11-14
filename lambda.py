{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "132c42b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06384a1c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "654187c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "66"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(lambda x,y:x+y)(10,56)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b161ec1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[16, 25, 36, 64]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "py=[4,5,6,8]\n",
    "list(map(lambda x:x*x,py))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d35d1337",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 3, 5]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "py=['java','sid','suraj']\n",
    "list(map(lambda x:len(x),py))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "05467b62",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['test', 'sample', 'test23', 'gcgf']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "py_file=['test.pdf','sample.xlsx','test23.pdf','gcgf.txt']\n",
    "list(map(lambda x:x.split('.')[0],py_file))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b77e3768",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['px', 'pf', 'gh']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p=['pxs456','pf7895','ghj4512']\n",
    "list(map(lambda x:x[0:2],p))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bd33d5b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "##element operation map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e21c0445",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2720213e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[56, 34, 6354, 74]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p=[56,34,75,6354,45,75,74]\n",
    "list(filter(lambda x:x%2==0,p))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "41ce76ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 1, 0, 0, 0, 0]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "py=['m','m','f','f','f','f']\n",
    "list(map(lambda x: 1 if x=='m'else 0,py))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ee2fb9da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[654648, 78246, 21468, 569746]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p=['654648','78246','21468','569746']\n",
    "list(map(lambda x:int(x),p))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02c95e16",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
