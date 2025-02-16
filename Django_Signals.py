## Question - 1

# -> By default, Django signals are executed synchronously. That means when signal is sent then the receiver function runs immediately after the signal is sent. Here in example it is
# shown that 
# Example : 
from django.dispatch import Signal, receiver
my_signal = Signal()

# Creating a receiver function
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received!")

# Sending the signal
print("Sending signal....")
my_signal.send(sender=None)
print("Signal sent!!!")


# OUTPUT
Sending signal...
Signal received!
Signal sent.
________________________________________
## Question - 2

# -> Yes, Django signals run in the same thread as the caller by default. That means when a signal is sent it execute within the same thread that invoked it. Here in example we can see
# while calling thread name before and after sending signal, which implies that signals runs in same thread as the caller by default
# Example :
import threading
from django.dispatch import Signal, receiver

my_signal = Signal()   # define a signal
 
@receiver(my_signal)   # creating receiver 
def my_receiver(sender, **kwargs):
    print(f"Receiver running in thread: {threading.current_thread().name}") # calling thread name after signal sent


print(f"Caller running in thread: {threading.current_thread().name}")  # calling thread name before signal sent
my_signal.send(sender=None)  # sending signal


# OUTPUT
Caller running in thread: MainThread
Receiver running in thread: MainThread


________________________________________
## Question - 3

# -> Yes, By default Django signals run in the same database transaction as the caller when they are triggered. That means if the caller roll back the transaction, the signal's 
# database changes will roll back and if transaction is committed then signal's database actions are committed as well.
# Example :
from django.db import transaction, models
from django.dispatch import Signal, receiver

my_signal = Signal() # Define a signal

# Createing receiver function
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver running in transaction: {transaction.get_autocommit()}")

# Sending signal inside a transaction
with transaction.atomic(): # Here atomic allows to create a block of code within which the atomicity on the database is guaranteed
    print(f"Caller running in transaction: {transaction.get_autocommit()}")
    my_signal.send(sender=None)

# OUTPUT
Caller running in transaction: False
Receiver running in transaction: False
