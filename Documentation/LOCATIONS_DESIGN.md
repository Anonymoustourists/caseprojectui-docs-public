# Locations Section Design

## Overview

The Locations section provides a centralized view of all geographic locations associated with People and Events in a case project. It features three viewing modes:

1. **Sidebar List View** - Compact list of all locations
2. **Spreadsheet View** - Detailed table with sortable columns
3. **Map View** - Interactive map with location pins and auto-zoom

## User Interface

### Sidebar (Left Panel)

- **Header**
  - "Locations" title
  - **Map/List Toggle Button** - Switches main view between list and map mode
  - **Expand Button** - Expands to spreadsheet view in main area
  - **Hide Button** - Collapses sidebar to icon

- **Location Count** - Shows "X of Y locations" when filters active

- **Filter Controls**
  - **Search Box** - Filter by name, type, city, county, or note
  - **Type Filter** - Dropdown: All Types, People Only, Events Only
  - **Date Range** - Two date inputs for filtering events by date
  - **Clear Filters** - Button appears when any filter is active

- **Location List**
  - Each item displays:
    - Pin icon (blue for People, purple for Events)
    - Name/label
    - Type/role (e.g., "Witness", "Factual Event")
    - Date (for events)
    - City, State (if available)
    - Location note (for people)
  - Click to select and highlight on map
  - Selected location has emerald background

### Main Content Area

#### List Mode (Default)
- Shows empty state with instructions when no location selected
- Prompts user to click map icon to view all locations

#### Spreadsheet Mode (Expanded)
- Full-width table with columns:
  - **Type** - Badge (Person/Event)
  - **Name** - Entity name
  - **Address** - Street address (if available)
  - **City** - City name
  - **County** - County name
  - **Date/Note** - Event date or person location note
  - **Coordinates** - Lat/lon in decimal degrees (4 decimals)
- Sticky header for scrolling
- Row hover effect
- Click row to select location

#### Map Mode
- **Interactive Map**
  - MapLibre GL base map
  - Navigation controls (zoom, compass)
  - Custom pin markers:
    - Blue pins for People locations
    - Purple pins for Event locations
  - **Auto-zoom to fit all locations** with padding
  - Maximum zoom level: 15 (prevents over-zooming on single location)
  - Smooth animation (1000ms duration)

- **Marker Interactions**
  - Click marker to select location
  - Selected marker scales up (1.2x) and gains high z-index
  - Popup shows:
    - Name/label (bold)
    - Type and date (if event)
    - City, state (if available)
    - Location note (if person)

- **Clustering** (when >= 10 locations)
  - **Green cluster markers** show count of grouped locations
  - Click cluster to zoom in and expand
  - Clusters update dynamically as map pans/zooms
  - **Toggle button** (top-right) to enable/disable clustering
  - Clustering parameters:
    - Radius: 60px
    - Max zoom: 16 (beyond this, always show individual markers)

- **Location Count Overlay** - Top-left corner shows "X locations"

## Data Sources

### People Locations
- Sourced from `Person.location` field
- Includes `Person.locationNote` for additional context
- Type derived from `Person.data.role` or `Person.data.relation`

### Event Locations
- Sourced from `EventItem.location` field
- Type derived from `EventItem.type` (e.g., "factual", "background", "investigatory")
- Includes `EventItem.date` for temporal context

## Technical Implementation

### Components

#### LocationsViewer.tsx
- **Path**: `src/pages/LocationsViewer.tsx`
- **Responsibilities**:
  - Fetch locations from People and Events APIs
  - Manage sidebar and view mode state
  - Coordinate between list, spreadsheet, and map views
- **State**:
  - `sidebarCollapsed` - Sidebar visibility
  - `sidebarExpanded` - Spreadsheet mode toggle
  - `viewMode` - "list" or "map"
  - `locations` - Combined array of LocationItems
  - `selectedLocationId` - Currently selected location

#### LocationsMapView.tsx
- **Path**: `src/components/Map/LocationsMapView.tsx`
- **Responsibilities**:
  - Render MapLibre GL map
  - Create and manage markers for each location
  - Handle marker selection and popup display
  - Auto-fit map bounds to show all locations
- **Key Features**:
  - Custom SVG pin markers (colored by type)
  - Popup HTML with rich location details
  - Marker click handlers
  - Selection highlighting (scale transform)
  - Error handling with fallback UI

### Routing

- **Route**: `/locations`
- **Navigation**: Sidebar "Locations" button (🗺️ icon)
- **History**: Pushes state to browser history for back/forward support

### Integration Points

1. **App.jsx**
   - Added `LocationsViewer` import
   - Added `openLocations` callback
   - Added `/locations` route handling
   - Added `onSelectLocations` prop to Sidebar

2. **Sidebar.tsx**
   - Added "Locations" button with map icon
   - Added `locations` to sections state
   - Added expand/collapse support for locations section

3. **APIs**
   - `listPeople(slug)` - Fetch all people with locations
   - `listEvents(slug)` - Fetch all events with locations
   - Filters out entities without location data

## Type Definitions

### LocationItem
```typescript
interface LocationItem {
  id: string;              // "person-123" or "event-456"
  label: string;           // Display name
  type: "person" | "event";
  typeName: string;        // Role/event type
  date?: string;           // For events
  note?: string;           // For people (locationNote)
  location: Location;      // Full location object
}
```

### Location (Existing)
```typescript
interface Location {
  lat: number;
  lon: number;
  label: string;
  source: "user" | "geocode" | "revgeocode";
  address?: Address;
  zoomHint?: number;
}
```

## User Workflows

### Viewing All Locations on Map
1. Navigate to Locations section (sidebar button)
2. Click map icon in sidebar header
3. Map displays all locations with auto-zoom to fit bounds
4. Click any marker to select and view details

### Finding a Specific Location
1. Navigate to Locations section
2. Scroll through sidebar list
3. Click location to select
4. Switch to map view to see pin on map (selected marker highlighted)

### Analyzing Location Data
1. Navigate to Locations section
2. Click expand button for spreadsheet view
3. View tabular data with all location attributes
4. Click row to select location
5. Switch back to map view to visualize

## Design Patterns

### Lazy Loading
- LocationsMapView is lazy-loaded with React.lazy() and Suspense
- Reduces initial bundle size
- Shows "Loading map..." fallback during import

### State Management
- Local component state for UI controls
- Project context for active project
- Async data fetching on mount and project change

### Responsive Design
- Sidebar collapses to icon when dismissed
- Spreadsheet view takes full width
- Map scales to container dimensions

### Error Handling
- Try-catch blocks around API calls
- Console logging for debugging
- Fallback UI for map initialization errors
- Graceful handling of missing data (filters, null checks)

## Implemented Features

### ✅ Filtering
- **Search** - Filter by name, type, city, county, or location note
- **Type Filter** - Show only People, only Events, or all types
- **Date Range Filter** - Filter events by date range
- **Clear Filters** - One-click reset of all filters
- **Live Updates** - Sidebar list, spreadsheet, and map all update with filters

### ✅ Clustering
- **Automatic Clustering** - Enabled by default when 10+ locations
- **Smart Grouping** - Uses Supercluster with 60px radius
- **Click to Expand** - Click clusters to zoom in and reveal individual markers
- **Dynamic Updates** - Clusters recalculate as map moves
- **Toggle Control** - Enable/disable clustering with button
- **Performance** - Only updates markers on map moveend for efficiency

## Future Enhancements

1. **Location Editing**
   - Edit location directly from spreadsheet
   - Click marker to edit associated entity

2. **Export**
   - Export to CSV/Excel
   - Export to KML for Google Earth

5. **Timeline Integration**
   - Click event marker to jump to timeline view
   - Show temporal flow of locations

6. **Heatmap Mode**
   - Visualize density of locations
   - Useful for cases with many addresses

## Dependencies

- **maplibre-gl**: ^5.x - Map rendering
- **supercluster**: ^8.x - High-performance marker clustering
- **@types/supercluster**: Type definitions for Supercluster
- **@types/geojson**: Type definitions for GeoJSON
- **React**: ^18.x - UI framework
- **Vite**: Build tooling and env vars

## Configuration

Maps functionality controlled by environment variables:
- `VITE_FEATURE_MAPS=1` - Enable maps features
- `VITE_MAPS_BASE_URL` - Base URL for map services
- `VITE_MAP_STYLE_PATH` - Path to map style JSON
- `VITE_AUTOCOMPLETE_PATH` - Photon autocomplete endpoint
- `VITE_GEOCODE_PATH` - Nominatim geocode endpoint
- `VITE_REVERSE_PATH` - Nominatim reverse geocode endpoint

## Testing Considerations

- Mock MapLibre GL in Vitest (handled in vitest.setup.ts)
- Test empty state rendering
- Test location list filtering
- Test marker creation and selection
- Test bounds calculation for auto-zoom
- Test spreadsheet sorting and row selection

## Accessibility

- Keyboard navigation support
- ARIA labels on interactive elements
- Semantic HTML structure
- Color contrast for text and icons
- Focus indicators on interactive elements

## Performance

- Lazy loading of map component
- Efficient marker management (Map data structure)
- Debounced search inputs (when filtering added)
- Optimized re-renders with useMemo and useCallback (when needed)
