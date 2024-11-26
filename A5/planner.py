from flight import Flight
from data_structures import Queue, PriorityQueue

class Planner:
    def __init__(self, flights):
        """The Planner
        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.m = len(flights)
        _ = max(flights, key = lambda x: max(x.start_city, x.end_city))
        self.n = max(_.start_city, _.end_city) + 1
        self.flights_from = [[] for i in range(self.n)]
        for f in flights: self.flights_from[f.start_city].append(f)
        
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        visited = [False]*self.m
        dist = [float('inf')]*self.m
        pred = [None]*self.m

        Q = Queue()

        for f in self.flights_from[start_city]:
            if f.departure_time >= t1 and f.arrival_time <= t2:
                visited[f.flight_no] = True
                dist[f.flight_no] = 0
                Q.enqueue(f)
        
        best_flight = None

        while not Q.is_empty():
            f = Q.dequeue()

            if best_flight is not None and dist[f.flight_no] > dist[best_flight.flight_no]: break

            if f.end_city == end_city:
                if best_flight is None or f.arrival_time < best_flight.arrival_time: best_flight = f
                else: continue

            for g in self.flights_from[f.end_city]:
                if visited[g.flight_no]: continue
                if g.departure_time >= f.arrival_time + 20 and g.arrival_time <= t2:
                    visited[g.flight_no] = True
                    dist[g.flight_no] = dist[f.flight_no] + 1
                    pred[g.flight_no] = f
                    Q.enqueue(g)

        return self.get_route(best_flight, pred)
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        cost = [float('inf')]*self.m
        pred = [None]*self.m
        processed = [False]*self.m

        pq = PriorityQueue(comparator = lambda x, y: x[0] < y[0])
        
        for f in self.flights_from[start_city]:
            if f.departure_time >= t1 and f.arrival_time <= t2:
                cost[f.flight_no] = f.fare
                pq.insert((f.fare, f))
        
        best_flight = None

        while not pq.is_empty():
            f = pq.remove_min()[1]

            if processed[f.flight_no]: continue
            processed[f.flight_no] = True

            if f.end_city == end_city: best_flight = f; break

            for g in self.flights_from[f.end_city]:
                if g.departure_time < f.arrival_time + 20 or g.arrival_time > t2: continue
                c = cost[f.flight_no] + g.fare
                if c < cost[g.flight_no]:
                    cost[g.flight_no] = c
                    pred[g.flight_no] = f
                    pq.insert((c, g))
        
        return self.get_route(best_flight, pred)

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        dist = [float('inf')]*self.m
        cost = [float('inf')]*self.m
        pred = [None]*self.m
        processed = [False]*self.m

        pq = PriorityQueue(comparator = lambda x, y: x[:-1] < y[:-1])
        
        for f in self.flights_from[start_city]:
            if f.departure_time >= t1 and f.arrival_time <= t2:
                dist[f.flight_no] = 0
                cost[f.flight_no] = f.fare
                pq.insert((0, f.fare, f))

        best_flight = None

        while not pq.is_empty():
            f = pq.remove_min()[-1]

            if processed[f.flight_no]: continue
            processed[f.flight_no] = True

            if f.end_city == end_city: best_flight = f; break
            
            for g in self.flights_from[f.end_city]:
                if g.departure_time < f.arrival_time + 20 or g.arrival_time > t2: continue
                d, c = dist[f.flight_no] + 1, cost[f.flight_no] + g.fare
                if (d, c) < (dist[g.flight_no], cost[g.flight_no]):
                    dist[g.flight_no], cost[g.flight_no] = d, c
                    pred[g.flight_no] = f
                    pq.insert((d, c, g))
        
        return self.get_route(best_flight, pred)
    
    def get_route(self, best_flight, pred):
        if best_flight is None: return []

        route = []
        f = best_flight

        while f != None: 
            route.append(f)
            f = pred[f.flight_no]

        return route[::-1]