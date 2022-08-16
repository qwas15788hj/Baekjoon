import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
		
	static class Room implements Comparable<Room> {
		int start, end;

		public Room(int start, int end) {
			super();
			this.start = start;
			this.end = end;
		}

		@Override
		public int compareTo(Room o) {
			return this.end != o.end ? this.end-o.end : this.start-o.start;
		}
		
	}//Room Class
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Room[] rooms = new Room[n];
		for(int i=0; i<n; i++) {
			rooms[i] = new Room(sc.nextInt(), sc.nextInt());
		}
		
		List<Room> result = getSchedule(rooms);
        
		System.out.println(result.size());
		
	}//main
	
	public static List<Room> getSchedule(Room[] rooms) {
		
		List<Room> result = new ArrayList<Room>();
		Arrays.sort(rooms);
		result.add(rooms[0]);
		
		for(int i=1; i<rooms.length; i++) {
			if(result.get(result.size()-1).end <= rooms[i].start) {
				result.add(rooms[i]);
			}
		}
		
		return result;
		
	}
	

}//class
