import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# FAQ data pulled from https://www.benchmarkclimbing.com/faqs on Dec 15, 2023.
context = '''Here's some context related to my business. 
                                  
QUESTION: What is bouldering?
ANSWER:Bouldering is a form of climbing where 8-16 foot walls are scaled over large foam “crash pads.” This form of climbing requires virtually no equipment—just climbing shoes and chalk! Bouldering requires creative problem solving, physical strength, balance, technique and mental fortitude. Most climbers would agree that bouldering is the most social of all climbing disciplines. It’s not uncommon to see groups of boulderers working together to unlock the subtleties of each climb, or bouldering “problems.”

QUESTION: What do I need for my first visit?
ANSWER:You must sign a facility waiver and present a valid government-issued photo-ID on your first visit. Waivers for minors must be signed by a parent or court appointed, legal guardian. There are no exceptions to this requirement. If you are completing a waiver on behalf of a minor as their court appointed legal guardian, please bring the appropriate court documentation.

If the parent or guardian will not be present, the minor must present a photocopy of the adult’s government-issued photo ID for signature verification.

To save time on your first visit, please create a customer account and sign our online waiver in advance. 

QUESTION: My child is interested in climbing. Does Benchmark allow children?
ANSWER:Yes! Please read Benchmark’s policies and guidelines on climbing with children here.

QUESTION: How do I become a member?
ANSWER:You can purchase a membership online through our membership page or stop by the gym and our front desk staff will be happy to assist you!

QUESTION: I signed up for the membership, how do I cancel it?
ANSWER:Customers wishing to freeze, cancel, or make changes to their memberships should login and submit a request through the support section of the customer portal. If you’d like to cancel your membership, you must notify us before your renewal date. Change requests that are sent on or after your renewal date will be processed for the following month. 

QUESTION: Can I freeze my membership?
ANSWER:All recurring EFT memberships are $10/month to freeze. We don't allow freezes for any prepaid memberships, with the exception of the annual prepaid, which is $15/month to freeze. All freezes go into effect within 72 hours of receiving your request. Please note that we are unable to freeze accounts that have outstanding/unpaid membership dues.

QUESTION: How do membership freezes work?
ANSWER:When you freeze your membership, you'll be charged the first freeze fee on your next renewal date. Upon reactivation, we’ll apply any credit days to your next bill and charge a prorated amount.

Extra credit days do not carry over. If you have more credit days than days remaining in the billing cycle, the prorated fee will be $0.

Please note that if you freeze and unfreeze in the same billing cycle (i.e. before the first freeze fee is charged), your membership will simply resume and no days will be credited.

QUESTION: Do you offer tours or can I visit the gym without a membership?
ANSWER:Yes! Feel free to drop in any time during business hours for a tour. You’ll be required to fill out a waiver at the front desk before you’re allowed to enter the gym.

QUESTION: What is the best way to get to Benchmark Van Ness?
ANSWER:Our SF gym is centrally located in San Francisco on the Van Ness artery which makes it easily accessible by foot, bike, public transit, or ride share. The 49 bus line drops off Van Ness & Sutter, 2 blocks away, and arrives every few minutes. 

Street parking is limited but there are parking garages nearby, the closest being 2 block away on Bush & Polk.

In 2022, Van Ness will be served by San Francisco’s first Bus Rapid Transit (BRT) system which will improve public transit service to our gym.

QUESTION: What are the gym policies around COVID-19?
ANSWER:Effective March 11, 2022, Benchmark is lifting its mask requirement for all members and guests. We do not require proof of vaccination to enter our facility.

QUESTION: Does the gym provide rental equipment?
ANSWER:Yes, guests can rent shoes and chalk bags for $5.

QUESTION: Are there bike racks?
ANSWER:Yes!! Bike racks are located directly outside of the SF gym on Van Ness Ave. and in the southern parking lot at our Berkeley location. While we hope to offer indoor bike storage in the future, please use the outdoor racks for now.

QUESTION: Do you offer any classes or coaching?
ANSWER:We offer Climbing Classes and Private Coaching for climbers of all ability levels. We also offer a variety of Group Packages (including private events!) for folks looking to gather their friends and/or colleagues and climb together!

QUESTION: How do I get in contact if I have other questions?
ANSWER:Feel free to email us at frontdesk@benchmarkclimbing.com and we’ll get back to you as soon as we can.

QUESTION: Can I bring my dog to Benchmark?
ANSWER:No. While we absolutely love dogs, we ask that you leave your furry friend at home so we can keep the gym environment safe and clean..

QUESTION: Can I bring outside food?
ANSWER:Yes! We encourage you to bring outside food and hang out before or after your session.

QUESTION: How often are the climbs reset?
ANSWER:Our SF and Berkeley gym are each on a 5 week setting rotation with fresh problems going up each week!                      

See if you can answer the following question with the context above. If the context doesn't fit exactly, but relates, you can extrapolate a bit to provide a more helpful answer. If you don't know, it's okay to say you don't know. Here's the question: '''

print("🧗‍♂️Welcome to Benchmark Climbing FAQ Bot!🧗‍♀️")
while True:
    userInput = input("> ")
    response = model.generate_content(f"{context} - {userInput}")

    print(response.text + "\n\n")

