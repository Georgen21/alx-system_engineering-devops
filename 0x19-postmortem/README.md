Postmortem:
WEB SERVER (LOAD BALANCER)
Issue Summary:
Duration: March 9, 2024, 10:00 AM - March 8, 2024, 2:00 AM (WAT)
Impact: The web application experienced intermittent downtime, resulting in slow response times and error messages.
Root Cause: A misconfigured load balancer caused uneven distribution of traffic, leading to overload on a server and subsequent service degradation.
Timeline:
10:00 AM: Issue detected by monitoring alert indicating increased error rates.
10:15 AM: I was notified of the issue via automated alert.
10:30 AM: Initial investigation focused on application servers due to elevated error rates.
11:00 AM: Load balancer configurations. I checked for abnormalities.
11:30 AM: Assumed database issues due to intermittent connection errors.
12:00 PM: Incident  investigated by me.
1:00 PM: Load balancer misconfiguration identified as root cause.
2:00 PM: Issue resolved by adjusting load balancer settings to evenly distribute traffic.
Root Cause and Resolution:
Root Cause: The load balancer was misconfigured to send a disproportionate amount of traffic to a certain server, leading to overload and service degradation.
Resolution: The load balancer setting was adjusted to evenly distribute traffic across the servers, restoring a normal operation.
Corrective and Preventative Measures:
Improvements/Fixes:
To regularly monitor or audit the  load balancer configurations to prevent similar misconfigurations and implement an automated monitoring load balancer to detect abnormalities promptly.
Summary:
This postmortem provides a detailed analysis of the recent web server outage incident during a project, including the duration, impact, root cause, timeline, resolution, and corrective/preventative measures. By identifying and addressing the misconfigured load balancer, I have taken steps to prevent similar incidents in the future and ensure the reliability and stability of  my web application.
