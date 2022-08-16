import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	static class Room implements Comparable<Room>{
		int start, end;

		public Room(int start, int end) {
			super();
			this.start = start;
			this.end = end;
		}

		@Override
		public int compareTo(Room o) {
			return this.start != o.start ? this.start-o.start : this.end-o.end;
		}
		
	}//Room Class
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Room[] rooms = new Room[n];
		for(int i=0; i<n; i++) {
			rooms[i] = new Room(sc.nextInt(), sc.nextInt());
		}
		
		Arrays.sort(rooms);
		
		PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
		queue.offer(rooms[0].end);
		
		for(int i=1; i<rooms.length; i++) {
			if(queue.peek() <= rooms[i].start) {
				queue.poll();
			}
			queue.offer(rooms[i].end);
		}
		
		System.out.println(queue.size());
//		List<Room> result = getCount(rooms);
//		System.out.println(result.size());
		
		
	}//main
	
//	public static List<Room> getCount(Room[] rooms) {
//		
//		List<Room> result = new ArrayList<Room>();
//		Arrays.sort(rooms);
//		result.add(rooms[0]);
//		
//		for(int i=1; i<rooms.length; i++) {
//			if(result.get(result.size()-1).end <= rooms[i].start) {
//				result.add(rooms[i]);
//			}
//		}
//		
//		
//		return result;
//	}//getCount
	
}//class
