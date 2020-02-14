import bme.mokk.hunmorph.HunmorphStub;
import bme.mokk.hunmorph.HunmorphStub.*;
import java.util.*;
import java.io.*;


public class TestHunmorphStub {

	static {
		System.loadLibrary("ocamorph");
	}

	public static void main(String[] args) {
		try {
			HunmorphStub stub = new HunmorphStub(args[0]); 
//			Analyzer analyzer = stub.createAnalyzer(Compounds.Allow, Guess.Fallback);
			Analyzer analyzer = stub.createAnalyzer(Compounds.No, Guess.NoGuess);
			List<String> result ;
			String encoding = "ISO-8859-2";
			BufferedReader input = new BufferedReader(new InputStreamReader(System.in, encoding));
			String line = null;
			while((line = input.readLine()) != null) {
				System.out.print(line);
				result = analyzer.analyze(line);
				System.out.println(result.size() + " analyses");
				for(String a : result) {
					System.out.print("\t" + a);
				}
				System.out.print("\n");
			}
		} catch (Exception e) {
			System.out.println("Exception caught: " + e);
		}
			
	}

}
