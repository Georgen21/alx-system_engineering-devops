#!/usr/bin/env ruby

log_line = "2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]' 12392190384,19148265919,-1:0:-1:-1:-1 $"

date_time = log_line.match(/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/)
sender = log_line.match(/\[from:(\d+)\]/)&.captures&.first
recipient = log_line.match(/\[to:(\d+)\]/)&.captures&.first
message = log_line.match(/\[msg:\d+:(.*?)\]/)&.captures&.first

puts "Date and Time: #{date_time}"
puts "Sender: #{sender}"
puts "Recipient: #{recipient}"
puts "Message: #{message}"
