<html>
    <body>
        <form method='POST'>
            Username: <input name='user'>
            <br><br>
            Password: <input type='password' name='pass'>
            <input type='submit'>
        </form>
        <?php
            if ($_SERVER["REQUEST_METHOD"] === 'POST'){
                $db = new SQLite3('users.db');
                $user = isset($_POST['user']) ? $_POST['user'] : '';
                $pass = isset($_POST['pass']) ? md5($_POST['pass']) : '';
                
                $query = $db->prepare("SELECT * from user WHERE username = :user AND password = :pass LIMIT 1");
                $query->bindValue(':user', $user);
                $query->bindValue(':pass', $pass);
                $result = $query->execute()->fetchArray();
                
                if ($result[0] === $user){
                    $flag = "GCTF{D0n7_Und3r3s71m4t3_7h3_p0w3r_0f_d1rec70r1e5}";
                    if ($_SERVER['HTTP_USER_AGENT'] === 'Mozilla/5.0 (SMART-TV; Ubuntu 12.04 LTS; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1') {
                        echo "Hello ". $user;
                        echo "<br />";
                        echo $flag;
                        echo "";
                    } else {
                        echo "Sorry your browser is not supported";
                    }
                } else {
                    echo 'Invalid Credentials';
                }
            }
        ?>
    </body>
</html>