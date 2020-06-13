<html>
    <body>
        <form>
            <input name='e'>
            <input type='submit'>
        </form>
        <?php
            if (isset($_GET['e'])) {
                $flag = 'GCTF{ev4l_4r3_d4ng3r0us)';
                $query =  $_GET['e'];
                $query = str_replace('(', '', $query);
                $query = str_replace(')', '', $query);
                $query = str_replace(';', '', $query);
                echo 'Result of ' . $query . ': ';
                eval('echo ' . $query . ';');
            }
        ?>
    </body>
</html>