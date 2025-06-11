import streamlit as st
import streamlit.components.v1 as components
import requests
import time
import subprocess
import socket

# Header
st.title("👨‍💻 Network Recon Utility Tool")
st.subheader(
    """ 
    **💪 :rainbow[What task would you like to execute?]**
    """
)

# Selection Menu
options = ["🔎 IP Lookup", "🔔 Ping Network Test", "🔢 DNS Lookup", "👤 Show User Agent"]
selection = st.pills("**Tasks**", options, selection_mode="single")

# 🔎 IP Lookup
if selection == "🔎 IP Lookup":
    ip = st.text_input("Enter an IP Address to Lookup:", placeholder="IP Address")

    if ip:
        with st.spinner("Getting Info...", show_time=True):
            try:
                r = requests.get(f"http://ip-api.com/json/{ip}")
                ip_data = r.json()
            except Exception as e:
                st.error(f"Data Not Found")
            time.sleep(1)
        

        if ":" in ip:
            ip_version = "IPv6"
        elif "." in ip:
            ip_version = "IPv4"
        else:
            ip_version = "Unrecognized Version"

        st.markdown(f"**IP Version:** {ip_version}")
            
        st.markdown(f"**Time Zone:** {ip_data['timezone']}")
        st.markdown(f"**Country:** {ip_data['country']}")
        st.markdown(f"**City:** {ip_data['city']}")
        st.markdown(f"**Zip:** {ip_data['zip']}")
        st.markdown(f"**Internet Service Provider:** {ip_data['isp']}")

# 🔔 Ping Network Test
elif selection == "🔔 Ping Network Test":
    ping_input = st.text_input("Enter an IP Address or Domain Name:", placeholder="google.com")

    if ping_input:
        try:
            ping_command = f"ping -c 5 {ping_input}"
            
            with st.spinner("Getting Info...", show_time=True):
                ping_result = subprocess.getoutput(ping_command)
                time.sleep(1)
            st.code(ping_result)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 🔢 DNS Lookup
elif selection == "🔢 DNS Lookup":
    domain = st.text_input("Enter a Domain Name:", placeholder="youtube.com")

    if domain:
        try:
            with st.spinner("Getting Data...", show_time=True):
                address_info = socket.getaddrinfo(domain, 443)
                ipv4_list = []
                ipv6_list = []
                for i in address_info:
                    family, _, _, _, address_tuple = i
                    ip = address_tuple[0]
                    if family == socket.AF_INET:
                        ipv4_list.append(ip)
                    elif family == socket.AF_INET6:
                        ipv6_list.append(ip)
                time.sleep(1)

            st.subheader("IPv4 Addresses:")
            if ipv4_list:
                for ip in set(ipv4_list): 
                    st.markdown(f"➡️&nbsp;&nbsp;{ip}")
            else:
                st.markdown("No IPv4 address found.")

            st.subheader("IPv6 Addresses:")
            if ipv6_list:
                for ip in set(ipv6_list):
                    st.markdown(f"➡️&nbsp;&nbsp;{ip}")
            else:
                st.markdown("No IPv6 address found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 👤 Show User Agent
elif selection == "👤 Show User Agent":
    components.html(
        """
        <div style="color: white; font-size: 16px; font-family: system-ui;">
            <span style="font-weight: bold">Your User Agent: </span>
            <script>
                document.write(navigator.userAgent);
            </script>
        </div>
        """
    )