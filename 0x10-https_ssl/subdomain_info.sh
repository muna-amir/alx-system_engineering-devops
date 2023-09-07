#!/bin/bash

# Function to display subdomain information
display_subdomain_info() {
    local domain="$1"
    local subdomain="$2"
    
    # Query the DNS records for the subdomain and extract the relevant information
    local record_info=$(dig +short "$subdomain.$domain")

    # Determine the record type (A or CNAME)
    local record_type
    if [[ $record_info =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        record_type="A"
    elif [[ $record_info =~ ^.*\. ]]; then
        record_type="CNAME"
    else
        record_type="Unknown"
    fi

    # Display the subdomain information
    echo "The subdomain $subdomain is a $record_type record and points to $record_info"
}

# Main script logic
if [ $# -lt 1 ]; then
    echo "Usage: $0 <domain> [subdomain]"
    exit 1
fi

domain="$1"

if [ $# -eq 1 ]; then
    # Display information for default subdomains
    display_subdomain_info "$domain" "www"
    display_subdomain_info "$domain" "lb-01"
    display_subdomain_info "$domain" "web-01"
    display_subdomain_info "$domain" "web-02"
else
    # Display information for the specified subdomain
    subdomain="$2"
    display_subdomain_info "$domain" "$subdomain"
fi

