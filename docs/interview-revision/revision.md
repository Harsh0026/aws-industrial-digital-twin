# Consolidated Project Revision

## Phase 1: Initial Python Simulator

### Implemented and verified
- Three assets: conveyor motor, pump, and compressor.
- One JSON event per machine per run.
- Script runs from both the simulator directory and repository root.
- Uses Python standard library only.

### Design decisions
- Asset inventory is separate from telemetry generation.
- Stable machine IDs identify equipment across events.
- Event IDs identify individual events; they can support deduplication,
  but deduplication logic is not implemented yet.
- UTC timestamps avoid ambiguity across time zones.
- Measurement field names include units.
- One JSON object per line supports streaming and line-based processing.
- Inventory path is resolved relative to the script, not the working directory.

### Useful commands
- python3 -m json.tool simulator/machines.json: validate inventory JSON syntax.
- python3 simulator/simulate.py: generate one event per machine.

### Interview questions
Q: Is a telemetry simulator a digital twin?
A: No. It generates input data. Our planned twin will maintain asset state,
   relationships, and health information using incoming events.

Q: Why separate machine ID from event ID?
A: Machine ID stays stable for an asset. Event ID identifies an individual
   event, including when that event is retried or replayed.

Q: Why run Python directly before adding Docker?
A: Validate application behavior first, then introduce packaging and runtime
   isolation as a separate engineering step.

### Current limitations
- Independent random readings with shared ranges across machine types.
- Every machine is always running.
- No continuous generation, MQTT, persistence, or inventory schema validation.
- Simulation ranges are illustrative, not equipment safety limits.
