
# -*- coding: utf-8 -*-
def test_print(this_arguement):
    if this_arguement == "Total Rooms":
        return "     is the total number of your properties rooms."
    if this_arguement == "Out of Service":
        return "     is the total number of your properties rooms that were undergoing maintenance or otherwise unavailable and cannot produce revenue in this period."
    if this_arguement == "Available Rooms":
        return "     is the total number of your properties rooms that were open and available to generate revenue in this period."
    if this_arguement == "Occupied Rooms":
        return "     is the total number of your properties rooms that were booked and unavailable in the period."
    if this_arguement == "Occupied Percent":
        return "     is a rate of the function of available occupied rooms as part of total rooms on property. "
    if this_arguement == "Room Revenue":
        return """     is the total revenue generated from occupied rooms from rack, corporate, 
                            foreign, group but excludes F&B, retail, spa or other profit centers."""
    if this_arguement == "Average Daily Rate ADR":
        return """     is a hotel performance metric that assesses the total guest room revenue for a specific period
                        as a function of actual occupied hotel rooms within the same timeframe."""
    if this_arguement == "Market ADR":
        return """      is a market sample of other hotels average daily rate or ADR often used to evaluate against as a performance measure.
                        It can be very useful in segment homogenous markets and tracked overtime as a guage (or elastic ruler) of seasonal market makers strategies.  """
    if this_arguement == "Revenue Per Available Room RevPAR":
        return """      accounts for the average daily rooms revenue generated per available room. 
                        This metric doesn’t account for other revenue centers such as F&B, spa or retail. Average RevPar varies widely by market. As a hotel performance metric, 
                        it differs by market, segment and timing and is a time-based snapshot of a hotel performance."""
    if this_arguement == "Market RevPar":
        return """     accounts for the average daily rooms revenue generated per available room by your competitors in a form fitting sample. 
                        This metric doesn’t account for other revenue centers such as F&B, spa or retail. Average RevPar varies widely by market. As a hotel performance metric, 
                        it differs by market, segment and timing and is a time-based snapshot of a hotel performance."""
    
    if this_arguement == "Average Occupancy Rate AOR":
        return """     is a percentage of the available rooms occupied for a specific period. 
                            It is calculated as total paid rooms occupied divided by total available rooms."""
    if this_arguement == "Gross Operating Profit per Available Room GOPPAR":
        return """     is a hotel performance metric that assesses the sum total of all revenue streams for a specific period
                        as a function of actual occupied hotel rooms within the same timeframe. Great GOPPARS are a sign of revenue flexing outside
                        of just rack rates as well as a sign of a well rounded go to market strategy that was effective."""
    if this_arguement == "Market Penetration Index MPI":
        return """     is a market occupancy metric to judge where you stand against the local and global competitive set. Staying above 100 means you are leading 
                      the market in fill rates, but a boat that is overfull may be dangerous to navigate. Used in conjuction with other metrics like ADR / Market ADR / REVPAR
                      will let you know if you are the Captain of a ship whose high occupancy is actually the tip of an iceburg below."""
    if this_arguement == "Average Rate Index":
        return """     is a composite competitve ADR metric that reveals where you stand against room rates in your local market. Riding the line will keep you full, but
                        be a pig and you may be on the way to slaughter. Stay too lean against the competition and starve through winter."""
    if this_arguement == "Revenue Generation Index RGI":
        return """     is hotel performance metric measures how a hotel’s RevPar compares to their competitive set. It measures a hotel’s fair market share of their segment’s 
                        (competitive set, market, submarket, etc.) revenue per available room. If a hotel is capturing its fair market share, the index will be 100; 
                        if capturing less than its fair market share, a hotel’s index will be less than 100; and if capturing more than its fair market share, a hotel’s index will be greater than 100."""
    if this_arguement == "Market Cost per Booking":
        return """     is one of the single greatest leaps in trackable ROI in the last 20 years for hoteliers. The ad spend cost per channel per room.
                           Attention is the new economy. Are you paying the right people the right amount for those eyes?"""
    if this_arguement == "Sentiment Analysis":
        return """     is what people say about you behind your back on the internet for all your friends to see. The positive the negative and the ugly. A metric to see
                       if the tea they are spilling is sweet or sour. Keep it 100 as the kids say and your reviews are glowing. 65 is not a pass."""
    if this_arguement == "Direct Revenue Ratio DRR":
        return """     is a metric measures the percentage of online revenue coming in directly vs expensive third-party channels. 
                        Is your public sentiment the issue? When is the last time you checked your website? Does your reservation button work!?  """
    if this_arguement == "Web Conversion":
        return """      calculates the number of unique website visitors that convert into bookings. Revenue originates from potential guests researching a property online. 
                        As a hotel’s digital front door, a website influences guests’ impression more than any other marketing asset.  According to Hospitality Times, the average 
                        conversion rate for hotel websites is about 2-3%. In other words, approximately 97% of visitors to a hotel’s website leave without making a reservation. 
                        AB test anyone??""" 
    if this_arguement == "Outlet Net Revenue":
        return """     Its nice when they are all sleeping but its hard to get the steak in them and the revenue out. How do you outlets stack up against the pillows?"""
   
    if this_arguement == "Total Revenue per Available Room TREVPAR":
        return """     This is the total revenue per available room. This metric is the sum total of net revenues from all operated departments plus rentals and other 
                        income per available room for the period divided by the total available rooms during the period. a.k.a Healfth.""" 
    else:
        return "   :new technology means new ways to capture novel metrics and squeeze the lemons to optimize to brand identity as well as profit. "
