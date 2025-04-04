# Last Edited: 30th March, 2025

WHITE = "\033[38;2;212;212;212m"
YELLOW = "\033[38;2;255;200m"
RED = "\033[38;2;200;0m"
lb = "\033[38;2;108;180;238m"
LIGHT_YELLOW = "\033[38;2;255;224;110m"

B = "\033[1m"
I = "\033[3m"
U = "\033[4m"
R = "\033[0m"

def info():
        print(f"\n{'='*90}\n")
        
        print(f"Author: {LIGHT_YELLOW}Raktimjyoti Sarma{WHITE}")
        
        print("\n\n\n")
        
        print(f"{B}Project Usage Management{R}")
        print("")
        print(f"March 2025")
        print("")
        print(f"{B}Summary:{R}")
        print("You are permitted to use and share this project, provided that you credit the original\nauthor and do not modify or redistribute altered versions. No warranties are provided.")
        print("")
        print(f"{'-'*90}")
        print("")
        print(f"{B}Terms of Use:{R}")
        print("")
        print(f"{lb}1.{WHITE} {B}{YELLOW}Usage Rights{WHITE}{R}")
        print(f"\tThis project is free to use for personal and educational purposes without any fees.\n\tContact the author for commerical uses. {I}(Email and Instagram mentioned below){R}")
        print("")
        print(f"{lb}2.{WHITE} {B}{YELLOW}Sharing{WHITE}{R}")
        print("\tYou may share the original, unmodified version of this project, provided that\n\tthis agreement remains intact and included with all copies.")
        print("")
        print(f"{lb}3.{WHITE} {B}{YELLOW}No Unauthorized Modifications{WHITE}{R}")
        print("\tModifying and redistributing altered versions of this project are strictly\n\tprohibited.If you wish to make changes, you must keepthem within your own work and\n\tnot distribute them.")
        print("")
        print(f"{lb}4.{WHITE} {B}{YELLOW}Attribution Requirement{WHITE}{R}")
        print("\tProper credit must be given to the original author (Raktim) in any use case,\n\tincluding but not limited to:")
        print("\n\t\t- Presentations, reports, and school submissions: Acknowledgment in a\n\t\t  references or credits section.")
        print("\t\t- Online posts or videos: A visible mention with a link to the original\n\t\t  source or the author's Instagram (@raktimjs).")
        print("")
        print(f"{lb}5.{WHITE} {B}{YELLOW}No Warranty & Liability Disclaimer{WHITE}{R}")
        print("\tThis project is provided \"as is,\" without warranties of any kind, express or\n\timplied. The author is not responsible for any issues, data loss, or unintended\n\tconsequences arising from its use.")
        print("")
        print(f"{B}Agreement:{R}")
        print(f"\tBy using this project, you acknowledge and agree to these terms. Failure to comply\n\tmayresult in consequences as deemed appropriate.")
        print("")
        print(f"{'-'*90}")
        print("")
        print("Drafted with the assistance of GPT o3-mini, but all rights and final authority remain with\nthe original author.\n\n")
        
        print(f"Email       :   {LIGHT_YELLOW}raktimunreal4@gmail.com{WHITE}")
        print(f"GitHub      :   {LIGHT_YELLOW}https://www.github.com/raktimjs", WHITE)
        print(f"Instagram   :   {LIGHT_YELLOW}https://www.instagram.com/raktimjs\n\n\n\n", WHITE)
        
        input("Press enter to continue...")
        __import__('os').system('cls')
