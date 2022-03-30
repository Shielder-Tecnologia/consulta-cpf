<?php 
if ($argc!=2) {
    echo "wrong usage\n";
    return;
}
$path = getcwd();
$command = escapeshellcmd($path . "/seleniumapp.py " . $argv[1]);
$output = shell_exec($command);
echo $output;

?>
