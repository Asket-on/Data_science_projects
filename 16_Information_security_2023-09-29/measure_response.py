import requests
import time
import numpy as np
from tqdm import tqdm

if __name__ == "__main__":
    # Example loan application
    application = {
    'destination_port': 61695.0,
 'flow_duration': -0.5518342971407962,
 'total_fwd_packets': -0.011077673772155452,
 'total_backward_packets': -0.010042649044294387,
 'total_length_of_fwd_packets': -0.05835036559938107,
 'total_length_of_bwd_packets': -0.0075681974569120096,
 'fwd_packet_length_max': -0.3024737264322934,
 'fwd_packet_length_min': -0.1955740980386478,
 'fwd_packet_length_mean': -0.2957664536636763,
 'fwd_packet_length_std': -0.2738414956560021,
 'bwd_packet_length_max': -0.5888936191195708,
 'bwd_packet_length_min': -0.4253986539756467,
 'bwd_packet_length_mean': -0.6321571518448401,
 'bwd_packet_length_std': -0.5553051419395553,
 'flow_bytes/s': -0.04012540113388594,
 'flow_packets/s': -0.23422563706995228,
 'flow_iat_mean': -0.3650828781581513,
 'flow_iat_std': -0.49816036251360396,
 'flow_iat_max': -0.5091540606493955,
 'flow_iat_min': -0.06891427987692811,
 'fwd_iat_total': -0.543697764109194,
 'fwd_iat_mean': -0.3794576471362779,
 'fwd_iat_std': -0.47830177352511705,
 'fwd_iat_max': -0.5046945359372973,
 'fwd_iat_min': -0.11547737036047882,
 'bwd_iat_total': -0.34184101453288834,
 'bwd_iat_mean': -0.22424207368977092,
 'bwd_iat_std': -0.26844631456465495,
 'bwd_iat_max': -0.2945414320107262,
 'bwd_iat_min': -0.10545131582198217,
 'fwd_psh_flags': -0.1952153696323982,
 'fwd_urg_flags': -0.0073730996556543174,
 'fwd_header_length': 0.002421252024718618,
 'bwd_header_length': 0.0023347873391814525,
 'fwd_packets/s': -0.23059636092281716,
 'bwd_packets/s': -0.08251131158292525,
 'min_packet_length': -0.44073215783753833,
 'max_packet_length': -0.601815072644177,
 'packet_length_mean': -0.6641344873725934,
 'packet_length_std': -0.6017821140316081,
 'packet_length_variance': -0.45083050909507033,
 'fin_flag_count': -0.2580491441119776,
 'syn_flag_count': -0.1952153696323982,
 'rst_flag_count': -0.011226371581743068,
 'psh_flag_count': -0.7802211743422491,
 'ack_flag_count': 1.318247995552346,
 'urg_flag_count': 3.940682291767219,
 'cwe_flag_count': -0.0073730996556543174,
 'ece_flag_count': -0.011226371581743068,
 'down/up_ratio': -1.0155888210092803,
 'average_packet_size': -0.6675499386985513,
 'avg_fwd_segment_size': -0.2957664536636763,
 'avg_bwd_segment_size': -0.6321571518448401,
 'fwd_header_length.1': 0.002421252024718618,
 'subflow_fwd_packets': -0.011077673772155452,
 'subflow_fwd_bytes': -0.05835036559938107,
 'subflow_bwd_packets': -0.010042649044294387,
 'subflow_bwd_bytes': -0.007571735613253154,
 'init_win_bytes_forward': -0.5360115696542689,
 'init_win_bytes_backward': 4.773837284194703,
 'act_data_pkt_fwd': -0.010133292835094319,
 'min_seg_size_forward': 0.0025438011042890098,
 'active_mean': -0.14864289627357533,
 'active_std': -0.09638720345161875,
 'active_max': -0.1605092950212702,
 'active_min': -0.12609977523250174,
 'idle_mean': -0.4848250167312815,
 'idle_std': -0.14823540746507793,
 'idle_max': -0.49483922206364617,
 'idle_min': -0.4662195076999952
    }

    # Location of my server
    url = "http://0.0.0.0:8989/predict"

    # Measure the response time
    all_times = []
    # For 1000 times
    for i in tqdm(range(1000)):
        t0 = time.time_ns() // 1_000_000
        # Send a request
        resp = requests.post(url, json=application)
        t1 = time.time_ns() // 1_000_000
        # Measure how much time it took to get a response in ms
        time_taken = t1 - t0
        all_times.append(time_taken)

    # Print out the results
    print("Response time in ms:")
    print("Median:", np.quantile(all_times, 0.5))
    print("95th precentile:", np.quantile(all_times, 0.95))
    print("Max:", np.max(all_times))
