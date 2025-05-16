Activity - Due date : 16 May 2025 - Share the result directly to me on Teams
Write a short scenario for an online paid table booking system in chain restaurants with designing the use case diagram and use case description. 


Short scenario
Famous eateries chain, “Locaovers” has 4 branches in New Zealand and introduces an online paid table booking system in each branch to prevent the longer waiting time for the customer through its website. 
The customers can view the available branches, check available time slots and reserve the table by paying the small of reservation fees. 
The reservation fee can be deducted later with the food charges. The customers can change a booking on the phone. The restaurant reserves the right to cancel and no refund with no circumstance. 
If the customer doesn’t show up on the date and time, the system will consider it as ‘No show’ and forfeit the deposit without refund. 
The admin of restaurants can manage table availability, bookings and payments (external system). The system supports real-time availability updates and confirms reservations via email. 

The use case descriptions
Actors : 	1. Customer
            2. Admis

Main uses cases : 
	        1. View branches (4 branches)
			2. View availability date/time
			3. Book table 
			4. Fill in customer information (Name, Phone number, E-mail)
			5. Calculating fee
            6. Make a payment
			7. Confirm reservation (via e-mail)
			8. View bookings
            9. Manage bookings
            10. Manage availability
			11. Manage booking status

Pre-condition : 
      The customers no need to register and log-in to the system
      The admin needs to log-in to the system to manage all of functions

Main flow :
 	  	    1. Customer selects the preferred restaurant branch
			2. Customer selects the preferred date and time
            3. Customer fills in the information such as Name, Phone number, Email, Number of guests and any special notes (special events/dietary requirements)
            4. System calculates reservation fee
            5. Customer is redirected to the payment gateway to complete the reservation payment
            6. After successful payment, the system send the reservation confirm email
            7. Admins need to log-in to the system to view/manage bookings and manage availability
 
Post-condition : The table is reserved and was marked as unavailable


