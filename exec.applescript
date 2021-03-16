(*
 * @Author: Cumelmell
 * @Date: 2021-03-16 10:53:38
 * @LastEditors: Cumelmell
 * @LastEditTime: 2021-03-16 10:55:40
 *)
on run argv
  set query to argv as text
  set AppleScript's text item delimiters to "-"
  set tips to text item 1 of query
  set command to text item 2 of query
  set username to text item 3 of query
  set pwd to text item 4 of query
  do shell script command user name username password pwd with administrator privileges
  return tips
end run