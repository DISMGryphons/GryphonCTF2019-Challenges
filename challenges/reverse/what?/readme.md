# What?

## Question text
My friend send me an app that contains a message but i could'nt seem to find it. Can you help me find?

## Hints

## Distribution
* Learn Math.apk

## Solution
1. Decompile the file using a java decompiler
2. Find the main activity using the Android Manifest File (Main activity is d!)
3. In d, nothing is special, move on to the class where the button is connected to, which is b!
4. b is the same as d, nothing special. Choose one of the classes to look (I will use f as an example)
5. If you actually used the app, f is actually the addition part of the app. Keeping this in mind, ignore methods b and c as they are probably only for the game part only
```
    package com.example.learnmath;
    import androidx.appcompat.app.*;
    import android.view.*;
    import java.util.*;
    import android.widget.*;
    import android.content.*;
    import java.io.*;
    import android.os.*;

    public class f extends AppCompatActivity
    {
        private Button a;
        private TextView b;
        private TextView d;
        private EditText e;
        private String f;
        private Boolean g;
        private String h;
        public String i;
        private String j;
        private int k;
        private int l;
        private int m;
        private int p;
        private int q;
        private int r;
        private ArrayList<String> s;
        private int t;
        
        public f() {
            super();
            this.h = "Score: ";
            this.i = "Time: ";
            this.j = "What is ";
            this.k = 90;
            this.p = 0;
            this.q = 0;
            this.r = 0;
            this.s = new ArrayList<String>();
            this.t = 0;
        }
        
        private void a() {
            this.a.setOnClickListener((View$OnClickListener)new f.f$1(this, new Date().getTime()));
            this.b();
        }
        
        static /* synthetic */ String access$000(final f f) {
            return f.f;
        }
        
        static /* synthetic */ String access$002(final f f, final String f2) {
            return f.f = f2;
        }
        
        static /* synthetic */ EditText access$100(final f f) {
            return f.e;
        }
        
        static /* synthetic */ Boolean access$200(final f f) {
            return f.g;
        }
        
        static /* synthetic */ Boolean access$202(final f f, final Boolean g) {
            return f.g = g;
        }
        
        static /* synthetic */ int access$300(final f f) {
            return f.l;
        }
        
        static /* synthetic */ int access$400(final f f) {
            return f.m;
        }
        
        static /* synthetic */ boolean access$500(final f f, final String s, final int n, final int n2) {
            return f.c(s, n, n2);
        }
        
        static /* synthetic */ void access$600(final f f, final boolean b, final int n) {
            f.e(b, n);
        }
        
        static /* synthetic */ void access$700(final f f, final boolean b) {
            f.f(b);
        }
        
        private void b() {
            final Random random = new Random();
            this.l = random.nextInt(100) + 1;
            this.m = random.nextInt(100) + 1;
            this.d.setText((CharSequence)String.format("%s%d+%d", this.j, this.l, this.m));
        }
        
        private boolean c(final String anObject, final int n, final int n2) {
            return Integer.toString(n + n2).equals(anObject);
        }
        
        private void e(final boolean b, int p2) {
            if (b) {
                final int r = this.r + 1;
                this.r = r;
                this.q += (int)Math.rint((r / 10 + 1) * 150 + (15 - p2) * 20 * (r / 50 + 1));
                final StringBuilder sb = new StringBuilder();
                sb.append(this.h);
                sb.append(this.q);
                this.b.setText((CharSequence)sb.toString());
                Toast.makeText((Context)this, (CharSequence)"Correct!", 1).show();
                this.e.setText((CharSequence)"");
            }
            else {
                this.r = 0;
                this.q -= 100;
                final StringBuilder sb2 = new StringBuilder();
                sb2.append(this.h);
                sb2.append(this.q);
                this.b.setText((CharSequence)sb2.toString());
                final StringBuilder sb3 = new StringBuilder();
                sb3.append("Wrong! Ans is ");
                sb3.append(this.l + this.m);
                Toast.makeText((Context)this, (CharSequence)sb3.toString(), 1).show();
                this.e.setText((CharSequence)"");
            }
            p2 = this.p + 1;
            this.p = p2;
            if (p2 == 32) {
                this.f(b);
                final Intent intent = new Intent((Context)this, (Class)k.class);
                intent.putExtra("f", this.q);
                intent.putExtra("g", "a");
                intent.putExtra("h", (Serializable)this.s);
                this.startActivity(intent);
            }
            else {
                this.a();
            }
        }
        
        private void f(final boolean b) {
            if (b) {
                try {
                    final String str = this.s.get(this.t);
                    if (str.length() < 8) {
                        final StringBuilder sb = new StringBuilder();
                        sb.append(str);
                        sb.append("1");
                        final String string = sb.toString();
                        this.s.remove(this.t);
                        this.s.add(string);
                    }
                    else {
                        ++this.t;
                        this.s.add("1");
                    }
                }
                catch (IndexOutOfBoundsException ex) {
                    this.s.add("1");
                }
            }
            else {
                try {
                    final String str2 = this.s.get(this.t);
                    if (str2.length() < 8) {
                        final StringBuilder sb2 = new StringBuilder();
                        sb2.append(str2);
                        sb2.append("0");
                        final String string2 = sb2.toString();
                        this.s.remove(this.t);
                        this.s.add(string2);
                    }
                    else {
                        ++this.t;
                        this.s.add("0");
                    }
                }
                catch (IndexOutOfBoundsException ex2) {
                    this.s.add("0");
                }
            }
        }
        
        protected void onCreate(final Bundle bundle) {
            super.onCreate(bundle);
            this.setContentView(2131492893);
            this.a = (Button)this.findViewById(2131296319);
            this.b = (TextView)this.findViewById(2131296324);
            this.d = (TextView)this.findViewById(2131296371);
            this.e = (EditText)this.findViewById(2131296262);
            final StringBuilder sb = new StringBuilder();
            sb.append(this.i);
            sb.append(this.k);
            this.d.setText((CharSequence)sb.toString());
            this.a();
        }
    }
```
6. As for e, only this part is important as it transfers data to the next activity
```
    p2 = this.p + 1;
    this.p = p2;
    if (p2 == 32) {
        this.f(b);
        final Intent intent = new Intent((Context)this, (Class)k.class);
        intent.putExtra("f", this.q);
        intent.putExtra("g", "a");
        intent.putExtra("h", (Serializable)this.s);
        this.startActivity(intent);
    }
    else {
        this.a();
    }
```
7. Here, after 32 rounds it goes into k and passes in f,g,h where f is the score of the player, g is unknown for now and h links to a ArrayList. What is this ArrayList about?
8. this.s is mainly only touched here
```
    private void f(final boolean b) {
        if (b) {
            try {
                final String str = this.s.get(this.t);
                if (str.length() < 8) {
                    final StringBuilder sb = new StringBuilder();
                    sb.append(str);
                    sb.append("1");
                    final String string = sb.toString();
                    this.s.remove(this.t);
                    this.s.add(string);
                }
                else {
                    ++this.t;
                    this.s.add("1");
                }
            }
            catch (IndexOutOfBoundsException ex) {
                this.s.add("1");
            }
        }
        else {
            try {
                final String str2 = this.s.get(this.t);
                if (str2.length() < 8) {
                    final StringBuilder sb2 = new StringBuilder();
                    sb2.append(str2);
                    sb2.append("0");
                    final String string2 = sb2.toString();
                    this.s.remove(this.t);
                    this.s.add(string2);
                }
                else {
                    ++this.t;
                    this.s.add("0");
                }
            }
            catch (IndexOutOfBoundsException ex2) {
                this.s.add("0");
            }
        }
    }
```

9. Here, strings are being added into the ArrayList based on whether you ans each qn correctly, adds "1" if correct "0" if wrong, each with a max size of 8. This probably means that s stores 4 byte values since there are 32 qns in total, making it up 32 bits!
10. Now lets look at k:
```
    package com.example.learnmath;

    import androidx.appcompat.app.*;
    import android.widget.*;
    import android.os.*;
    import java.util.*;
    import android.view.*;
    import android.content.*;

    public class k extends AppCompatActivity
    {
        private int b;
        private int c;
        private String d;
        private TextView e;
        private Button f;
        private ArrayList<String> h;
        private String i;
        private String j;
        private String[] k;
        
        public k() {
            super();
            this.j = "byee";
            this.k = new String[] { "w", "x", "y", "z" };
        }
        
        protected void onCreate(final Bundle bundle) {
            super.onCreate(bundle);
            final SharedPreferences sharedPreferences = this.getSharedPreferences("Hello", 0);
            this.setContentView(2131492896);
            final Intent intent = this.getIntent();
            this.b = intent.getIntExtra("f", 0);
            this.d = intent.getStringExtra("g");
            this.e = (TextView)this.findViewById(2131296319);
            this.f = (Button)this.findViewById(2131296262);
            this.h = (ArrayList<String>)intent.getStringArrayListExtra("h");
            final byte[] bytes = this.j.getBytes();
            final byte[] a2 = new byte[4];
            int n = 0;
            while (true) {
                final String[] k = this.k;
                if (n >= k.length) {
                    break;
                }
                a2[n] = Integer.parseInt(sharedPreferences.getString(String.valueOf(k[n]), "0"), 2).byteValue();
                ++n;
            }
            if (Arrays.equals(bytes, a2)) {
                this.e.setText(2131623936);
            }
            else {
                this.f.setOnClickListener((View$OnClickListener)new k.k$1(this));
                final String d = this.d;
                final int hashCode = d.hashCode();
                int n2;
                if ((hashCode == 97) ? d.equals("a") : ((hashCode == 100) ? d.equals("d") : ((hashCode == 109) ? d.equals("m") : (hashCode == 115 && d.equals("s"))))) {
                    n2 = 1;
                }
                else {
                    n2 = -1;
                }
                if (n2 != 0) {
                    if (n2 != 1) {
                        if (n2 != 2) {
                            if (n2 == 3) {
                                this.c = sharedPreferences.getInt("d", 0);
                                this.i = this.h.get(1);
                                sharedPreferences.edit().putString("z", this.i).apply();
                            }
                        }
                        else {
                            this.c = sharedPreferences.getInt("m", 0);
                            this.i = this.h.get(2);
                            sharedPreferences.edit().putString("y", this.i).apply();
                        }
                    }
                    else {
                        this.c = sharedPreferences.getInt("s", 0);
                        this.i = this.h.get(3);
                        sharedPreferences.edit().putString("x", this.i).apply();
                    }
                }
                else {
                    this.c = sharedPreferences.getInt("a", 0);
                    this.i = this.h.get(0);
                    sharedPreferences.edit().putString("w", this.i).apply();
                }
                final int b = this.b;
                if (b > this.c) {
                    sharedPreferences.edit().putInt(this.d, this.b).apply();
                    this.e.setText((CharSequence)String.format("Congrats!\nYou have broken your highscore!\nYou have scored: %d", this.b));
                }
                else {
                    this.e.append((CharSequence)Integer.toString(b));
                }
            }
        }
    }
   
```

11. Here, it can be seen that:
    1.  This class is used to show the score
    2.  g is probably which activity it comes from
12. Now, here is the interesting part:
```
    final byte[] bytes = this.j.getBytes();
    final byte[] a2 = new byte[4];
    int n = 0;
    while (true) {
        final String[] k = this.k;
        if (n >= k.length) {
            break;
        }
        a2[n] = Integer.parseInt(sharedPreferences.getString(String.valueOf(k[n]), "0"), 2).byteValue();
        ++n;
    }
    if (Arrays.equals(bytes, a2)) {
        this.e.setText(2131623936);
    }
```
13. Here, it compares a byte array which is derived from the string "byee" to another byte array which is derived from a sharedpreference with keys of w,x,y and z. If its correct, it will deviate from the normal showing of the score to another view. The keys are being stored here:
```
     if (n2 != 0) {
        if (n2 != 1) {
            if (n2 != 2) {
                if (n2 == 3) {
                    this.c = sharedPreferences.getInt("d", 0);
                    this.i = this.h.get(1);
                    sharedPreferences.edit().putString("z", this.i).apply();
                }
            }
            else {
                this.c = sharedPreferences.getInt("m", 0);
                this.i = this.h.get(2);
                sharedPreferences.edit().putString("y", this.i).apply();
            }
        }
        else {
            this.c = sharedPreferences.getInt("s", 0);
            this.i = this.h.get(3);
            sharedPreferences.edit().putString("x", this.i).apply();
        }
    }
    else {
        this.c = sharedPreferences.getInt("a", 0);
        this.i = this.h.get(0);
        sharedPreferences.edit().putString("w", this.i).apply();
    }
```
14. Looking from here, the program grabs the first byte of the Array and stores in w, which is the first byte of the array! Hence, to get it, we will have to get the byte value of the character b, then convert it to binary to get the sequence of right and wrong answers we will need to get it the value.
15. The binary value of b is 01100010 so it will be 
    1.  wrong
    2.  right
    3.  right
    4.  wrong
    5.  wrong
    6.  wrong
    7.  right
    8.  wrong
    9.  for the rest of the 24 qn can just press submit repeatedly as they would not be used by this the program
16. Using the same logic for the rest of the classes you will derive this sequences for them
    1.  Subtraction class (last byte used,"y","01111001")
        1.  24 wrong
        2.  wrong
        3.  right
        4.  right
        5.  right
        6.  right
        7.  wrong
        8.  wrong
        9.  right
    2.  Multiplication class (3rd byte used, "e","01100101")
        1.  16 wrong
        2.  wrong
        3.  right
        4.  right
        5.  wrong
        6.  wrong
        7.  right
        8.  wrong
        9.  right
        10. 8 wrong
    3.  Division class (2nd byte used,"e","01100101")
        1.  8 wrong
        2.  wrong
        3.  right
        4.  right
        5.  wrong
        6.  wrong
        7.  right
        8.  wrong
        9.  right
        10. 16 wrong

17. If everything goes right, run the quiz once again you  will get this screen which shows you the flag:



## Flag
GCTF{pik4_p1ka_pika_piiik444chuuu!}
