public class Tutorial {

	public static void main(String[] args) {
		print();
	}

	private static void print() {
		//출력
		System.out.println("Hello World!");
		
		//변수 출력
		int num = 1;
		String name = "KimSungHyun";
		System.out.println(num);
		System.out.println(name);

		//문자열 반복
		System.out.println(repeat(name, 2)); //KimSungHyunKimSungHyun
		System.out.println(repeat("=", 10)); //==========

	}

	public static String repeat(String str, int times) {
        	return new String(new char[times]).replace("\0", str);
    	}
}
