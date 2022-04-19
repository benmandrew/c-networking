
#ifndef DEF_H
#define DEF_H

#include <assert.h>

#define HB_PORT 45000
#define HB_SIZE sizeof(int)
#define LSA_PORT 45001

#define MS2NS 1e+6

// Heartbeat period
#define HEARTBEAT_T (250 * MS2NS)
// Add a bit of fudge factor
#define HEARTBEAT_TIMEOUT (900 * MS2NS)
// How often we recompute the link metric
#define METRIC_RECOMPUTATION_T (50 * MS2NS)
// How often we send LSAs
#define LSA_SEND_T (50 * MS2NS)
// How long after the link comes up that we replay the buffered packets
#define REPLAY_DELAY_T (5 * MS2NS)

#define LOGGING_ACTIVE

// Maximum number of nodes in the network
#define MAX_NODE_NUM 12
// Maximum number of neighbours
#define MAX_NODE_FAN 6

#endif
