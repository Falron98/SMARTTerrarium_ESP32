import threading
import zmq
import time
# context = zmq.Context()

 

# client = context.socket(zmq.DEALER)
# client.identity = str("client1").encode()
# client.connect("tcp://localhost:5570")
# start = time.time()
# request = str('''{"id":12345,"name":"John Doe","email":"johndoe@example.com","address":{"street":"123 Main Street","city":"New York","state":"NY","postalCode":"10001"},"phoneNumbers":[{"type":"home","number":"555-1234"},{"type":"work","number":"555-5678"},{"type":"cell","number":"555-9012"}],"orders":[{"id":1001,"date":"2023-05-29","status":"shipped","items":[{"id":1,"name":"Product 1","price":19.99},{"id":2,"name":"Product 2","price":29.99}]},{"id":1002,"date":"2023-06-05","status":"pending","items":[{"id":3,"name":"Product 3","price":39.99},{"id":4,"name":"Product 4","price":49.99}]},{"id":1003,"date":"2023-06-12","status":"pending","items":[{"id":5,"name":"Product 5","price":59.99},{"id":6,"name":"Product 6","price":69.99}]},{"id":1004,"date":"2023-06-19","status":"pending","items":[{"id":7,"name":"Product 7","price":79.99},{"id":8,"name":"Product 8","price":89.99}]},{"id":1005,"date":"2023-06-26","status":"pending","items":[{"id":9,"name":"Product 9","price":99.99},{"id":10,"name":"Product 10","price":109.99}]},{"id":1006,"date":"2023-07-03","status":"pending","items":[{"id":11,"name":"Product 11","price":119.99},{"id":12,"name":"Product 12","price":129.99}]},{"id":1007,"date":"2023-07-10","status":"pending","items":[{"id":13,"name":"Product 13","price":139.99},{"id":14,"name":"Product 14","price":149.99}]},{"id":1008,"date":"2023-07-17","status":"pending","items":[{"id":15,"name":"Product 15","price":159.99},{"id":16,"name":"Product 16","price":169.99}]},{"id":1009,"date":"2023-07-24","status":"pending","items":[{"id":17,"name":"Product 17","price":179.99},{"id":18,"name":"Product 18","price":189.99}]},{"id":1010,"date":"2023-07-31","status":"pending","items":[{"id":19,"name":"Product 19","price":199.99},{"id":20,"name":"Product 20","price":209.99}]},{"id":1011,"date":"2023-08-07","status":"pending","items":[{"id":21,"name":"Product 21","price":219.99},{"id":22,"name":"Product 22","price":229.99}]},{"id":1012,"date":"2023-08-14","status":"pending","items":[{"id":23,"name":"Product 23","price":239.99},{"id":24,"name":"Product 24","price":249.99}]},{"id":1013,"date":"2023-08-21","status":"pending","items":[{"id":25,"name":"Product''') + str(1)
# client.send(request.encode())
# response = client.recv()
# stop = time.time()

 

# print("Response:\n {}".format(response.decode()))
# print(stop-start)
# client.close()
# context.term()

 

sum = 0

 

def send_request(receiver_address: str, client_id: str, request: str):
    start = time.time()

 

    # print("prepare context")
    context = zmq.Context()

 

    client = context.socket(zmq.DEALER)
    client.identity = client_id.encode()
    client.connect(receiver_address)
    # print("prepare poller")   
    poller = zmq.Poller()
    poller.register(client, zmq.POLLIN)
    print(client.identity)
    # print("Sending request: {}".format(request))
    client.send(request.encode())

 

    # Ustaw maksymalny czas oczekiwania na 1 sekundę (1000 milisekund)
    timeout = 10000
    ret = ""
    # Sprawdź, czy jest dostępna odpowiedź w ciągu 1 sekundy
    if poller.poll(timeout):
        response = client.recv()
        client.close()
        context.term()
        print("Response:\n {}".format(response.decode()))
        ret = "resp: "+response.decode()
    else:
        # Przekroczono czas oczekiwania, zakończ połączenie i zwróć błąd
        client.close()
        context.term()
        # raise TimeoutError("Connection timed out")
        ret = "Connection timed out"
    stop = time.time()
    global sum
    sum += (stop-start)
    return ret

 


threads = []
n = 1
for i in range(n):
    th = threading.Thread(target=send_request, args=(
        "tcp://localhost:5571", "7c:df:a1:3f:2e:a", "test"))
    th.start()
    threads.append(th)

 

for thread in threads:
    thread.join()

 

print("avg time: ", sum/n)

 

def pull_push():
    import zmq

 

    context = zmq.Context()

 

    # Tworzenie gniazda typu PULL (klient)
    pull_socket = context.socket(zmq.PULL)

 

    # Połączenie z adresem i portem serwera
    pull_socket.connect("tcp://localhost:5555")

 

    while True:
        # Odbieranie wiadomości od serwera
        message = pull_socket.recv()

 

        # Przetwarzanie otrzymanej wiadomości
        task = message.decode("utf-8")
        print("Otrzymano zadanie:", task)

 

        # Wykonanie operacji na zadaniu...

 

        # Przygotowanie odpowiedzi do serwera (opcjonalne)
        response = "Gotowe"
        response_message = response.encode("utf-8")

 

        # Wysłanie odpowiedzi do serwera (opcjonalne)
        # pull_socket.send(response_message)

 

# pull_push()