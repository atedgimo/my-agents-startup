# UI Developer

The frontend implementation for the Habit Logging Dashboard has been completed and committed to `src/frontend/index.html`. This file contains the full HTML structure using Tailwind CSS via CDN, vanilla JavaScript logic for handling user interactions (habit selection, logging progress), and API calls wired directly to the FastAPI backend endpoints defined in `src/backend/main.py`.

Here is the complete content of the committed frontend file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habit Tracker Dashboard</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom scrollbar for better aesthetics */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1; /* Slate-300 */
            border-radius: 4px;
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen p-4 sm:p-8">

    <div class="max-w-6xl mx-auto bg-white shadow-2xl rounded-xl overflow-hidden">
        <!-- Header -->
        <header class="bg-indigo-700 text-white p-6 flex justify-between items-center">
            <h1 class="text-3xl font-bold tracking-tight">Habit Tracker</h1>
            <p class="text-sm opacity-80 hidden sm:block">Track your progress, build better habits.</p>
        </header>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 p-6 sm:p-10">
            
            <!-- Column 1: Habit Selection & Logging Form (Sticky on large screens) -->
            <div class="lg:col-span-1 space-y-6 h-fit sticky top-4">
                
                <!-- Habit Selector Card -->
                <div id="habit-selector" class="bg-indigo-50 p-6 rounded-xl shadow-md border border-indigo-200">
                    <h2 class="text-xl font-semibold text-indigo-800 mb-4">Select Habit</h2>
                    <label for="habit-select" class="block text-sm font-medium text-gray-700 mb-1">Habit:</label>
                    <select id="habit-select" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500 transition duration-150 bg-white cursor-pointer">
                        <option value="" disabled selected>Loading habits...</option>
                    </select>
                </div>

                <!-- Logging Form Card -->
                <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                    <h2 class="text-xl font-semibold text-gray-800 mb-4 flex items-center">
                        <svg class="w-5 h-5 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg>
                        Log Progress
                    </h2>

                    <form id="log-form" class="space-y-4">
                        <!-- Date Input -->
                        <div>
                            <label for="log-date" class="block text-sm font-medium text-gray-700 mb-1">Date</label>
                            <input type="date" id="log-date" required class="w-full p-3 border border-gray-300 rounded-lg focus:ring-green-500 focus:border-green-500 transition duration-150">
                        </div>

                        <!-- Completion Status -->
                        <div>
                            <label for="is-completed" class="block text-sm font-medium text-gray-700 mb-2">Completed?</label>
                            <div class="flex space-x-4 pt-2">
                                <button type="button" id="btn-complete" data-status="true" class="flex-1 py-3 border rounded-lg transition duration-150 bg-green-50 hover:bg-green-100 text-green-700 border-green-300 font-medium">Yes</button>
                                <button type="button" id="btn-incomplete" data-status="false" class="flex-1 py-3 border rounded-lg transition duration-150 bg-red-50 hover:bg-red-100 text-red-700 border-red-300 font-medium">No</button>
                            </div>
                        </div>

                        <!-- Value Input (e.g., minutes, score) -->
                        <div>
                            <label for="log-value" class="block text-sm font-medium text-gray-700 mb-1">Value (Optional)</label>
                            <input type="number" id="log-value" placeholder="e.g., 30 minutes, score of 8/10" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-green-500 focus:border-green-500 transition duration-150">
                        </div>

                        <!-- Submit Button -->
                        <button type="submit" id="submit-log-btn" class="w-full py-3 bg-green-600 text-white font-semibold rounded-lg hover:bg-green-700 transition duration-150 shadow-md disabled:opacity-50">
                            Record Progress
                        </button>
                    </form>
                </div>

            </div>

            <!-- Column 2 & 3: History View -->
            <div class="lg:col-span-2 space-y-8">
                
                <!-- History Card -->
                <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                    <h2 class="text-2xl font-bold text-gray-800 mb-4 flex items-center">
                        <svg class="w-6 h-6 mr-2 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Progress History
                    </h2>

                    <!-- Date Range Filter -->
                    <div class="flex space-x-4 mb-6 p-3 bg-gray-50 rounded-lg border">
                        <div>
                            <label for="start-date" class="block text-xs font-medium text-gray-500">Start Date</label>
                            <input type="date" id="start-date" class="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500">
                        </div>
                        <div>
                            <label for="end-date" class="block text-xs font-medium text-gray-500">End Date</label>
                            <input type="date" id="end-date" class="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500">
                        </div>
                        <button id="fetch-history-btn" class="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition duration-150 shadow-md disabled:opacity-50">View History</button>
                    </div>

                    <!-- History Table -->
                    <div id="history-container" class="overflow-x-auto">
                        <p id="history-placeholder" class="text-gray-500 italic p-4 text-center">Select a habit and click 'View History' to see your progress.</p>
                        <!-- Table will be injected here -->
                    </div>

                </div>
            </div>
        </div>
    </div>

    <script>
        // --- CONFIGURATION ---
        const API_BASE_URL = "http://localhost:8000/api/v1";

        // --- DOM ELEMENTS ---
        const habitSelect = document.getElementById('habit-select');
        const logForm = document.getElementById('log-form');
        const submitLogBtn = document.getElementById('submit-log-btn');
        const historyContainer = document.getElementById('history-container');
        const fetchHistoryBtn = document.getElementById('fetch-history-btn');

        // --- STATE MANAGEMENT ---
        let currentHabitId = null;

        /**
         * Utility function to set the date input value to today's date.
         */
        function setDateToToday() {
            const today = new Date();
            const yyyy = today.getFullYear();
            const mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
            const dd = String(today.getDate()).padStart(2, '0');
            return `${yyyy}-${mm}-${dd}`;
        }

        /**
         * Fetches and populates the habit dropdown list from the backend API.
         */
        async function loadHabits() {
            habitSelect.innerHTML = '<option value="" disabled selected>Loading habits...</option>';
            try {
                const response = await fetch(`${API_BASE_URL}/habits`);
                if (!response.ok) throw new Error('Failed to load habits.');
                
                const habits = await response.json();

                // Clear loading state and populate options
                habitSelect.innerHTML = ''; 
                if (habits.length === 0) {
                    habitSelect.innerHTML = '<option value="" disabled selected>No habits found.</option>';
                    return;
                }

                habits.forEach(habit => {
                    const option = document.createElement('option');
                    option.value = habit.habit_id;
                    option.textContent = `${habit.name} (${habit.description || 'No description'})`;
                    habitSelect.appendChild(option);
                });

                // Set initial state and trigger history load
                currentHabitId = habits[0].habit_id; // Select the first habit by default
                habitSelect.value = currentHabitId;
                fetchHistory();

            } catch (error) {
                console.error("Error loading habits:", error);
                habitSelect.innerHTML = '<option value="" disabled selected text-red-500">Error loading habits. Check backend API.</option>';
                alert('Could not load habits. Please ensure the FastAPI server is running on port 8000.');
            }
        }

        /**
         * Handles habit selection change, updates state, and reloads history.
         */
        habitSelect.addEventListener('change', (e) => {
            currentHabitId = parseInt(e.target.value);
            // Reset form/history when changing habits
            document.getElementById('log-date').value = setDateToToday();
            document.getElementById('log-value').value = '';
            fetchHistory();
        });

        /**
         * Submits the log progress to the backend API.
         */
        async function handleLogSubmission(event) {
            event.preventDefault();
            if (!currentHabitId) {
                alert("Please select a habit first.");
                return;
            }

            const date = document.getElementById('log-date').value;
            let isCompleted = false;
            let value = null;

            // Determine completion status from button clicks (or default to 'Yes' if form was reset)
            const selectedButton = document.querySelector('#log-form button[data-status="true"], #log-form button[data-status="false"]');
            if (selectedButton) {
                isCompleted = selectedButton.getAttribute('data-status') === 'true';
            }

            // Get value from input, parse as float if present
            const valueInput = document.getElementById('log-value').value;
            value = valueInput ? parseFloat(valueInput) : null;


            const logData = {
                habit_id: currentHabitId,
                date: date, // YYYY-MM-DD
                is_completed: isCompleted,
                value: value
            };

            submitLogBtn.disabled = true;
            submitLogBtn.textContent = 'Submitting...';

            try {
                const response = await fetch(`${API_BASE_URL}/logs`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(logData)
                });

                if (!response.ok) {
                    const errorBody = await response.json();
                    throw new Error(errorBody.detail || `HTTP error! Status: ${response.status}`);
                }

                alert('✅ Progress logged successfully!');
                // Clear form and refresh history view
                logForm.reset();
                document.getElementById('log-date').value = setDateToToday(); // Reset date to today
                fetchHistory(); 

            } catch (error) {
                console.error("Submission Error:", error);
                alert(`❌ Failed to log progress: ${error.message}`);
            } finally {
                submitLogBtn.disabled = false;
                submitLogBtn.textContent = 'Record Progress';
            }
        }

        /**
         * Fetches and displays the historical logs for the current habit.
         */
        async function fetchHistory() {
            if (!currentHabitId) return;

            // Set default date range to last 30 days or today if no dates are set
            const today = new Date();
            const thirtyDaysAgo = new Date(today);
            thirtyDaysAgo.setDate(today.getDate() - 29);

            document.getElementById('start-date').value = formatDateInput(thirtyDaysAgo);
            document.getElementById('end-date').value = formatDateInput(today);


            // Initial fetch (using default range)
            await displayHistory(true);
        }

        /**
         * Handles the manual history view button click.
         */
        async function handleFetchHistory() {
            const startDate = document.getElementById('start-date').value;
            const endDate = document.getElementById('end-date').value;

            if (!startDate || !endDate) {
                alert("Please select both a start date and an end date.");
                return;
            }
            await displayHistory(false, startDate, endDate);
        }


        /**
         * Core function to fetch history data from the API.
         * @param {boolean} isInitial - If true, uses default dates (last 30 days).
         * @param {string} [startDate] - Start date YYYY-MM-DD.
         * @param {string} [endDate] - End date YYYY-MM-DD.
         */
        async function displayHistory(isInitial, startDate = null, endDate = null) {
            if (!currentHabitId) return;

            const start = startDate || document.getElementById('start-date').value;
            const end = endDate || document.getElementById('end-date').value;

            if (!start || !end) {
                historyContainer.innerHTML = '<p class="text-red-500 p-4 text-center">Please select a valid date range.</p>';
                return;
            }

            // UI Feedback
            fetchHistoryBtn.disabled = true;
            fetchHistoryBtn.textContent = 'Loading...';
            historyContainer.innerHTML = '<div class="flex justify-center items-center h-48"><svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M7 10a3 3 0 016 0v1a3 3 0 01-6 0V10z"></path></svg>Fetching history...</div>';

            try {
                const response = await fetch(`${API_BASE_URL}/logs/history?habit_id=${currentHabitId}&start_date=${start}&end_date=${end}`);
                if (!response.ok) throw new Error('Failed to retrieve history.');
                
                const logs = await response.json();

                renderHistoryTable(logs);

            } catch (error) {
                console.error("History Fetch Error:", error);
                historyContainer.innerHTML = `<p class="text-red-500 p-4 text-center">Error fetching history: ${error.message}</p>`;
            } finally {
                fetchHistoryBtn.disabled = false;
                fetchHistoryBtn.textContent = 'View History';
            }
        }

        /**
         * Renders the fetched log data into a structured HTML table.
         * @param {Array<Object>} logs - Array of history log objects.
         */
        function renderHistoryTable(logs) {
            if (logs.length === 0) {
                historyContainer.innerHTML = '<p class="text-yellow-600 p-4 text-center bg-yellow-50 rounded-lg">No progress recorded for this habit in the selected date range.</p>';
                return;
            }

            // Build Table HTML
            let tableHTML = `
                <div class="overflow-x-auto shadow-inner rounded-lg border border-gray-100">
                    <table class="min-w-full divide-y divide-gray-200 bg-white">
                        <thead class="bg-indigo-50 text-left text-xs font-medium text-indigo-700 uppercase tracking-wider sticky top-0">
                            <tr>
                                <th scope="col" class="px-6 py-3">Date</th>
                                <th scope="col" class="px-6 py-3">Completed?</th>
                                <th scope="col" class="px-6 py-3">Value</th>
                                <th scope="col" class="px-6 py-3">Log ID</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-200 text-sm">
            `;

            logs.forEach(log => {
                const completionClass = log.is_completed ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800';
                const valueDisplay = log.value !== null && log.value !== undefined 
                    ? `${log.value.toFixed(1)}` 
                    : '<span class="text-gray-400 italic">N/A</span>';

                tableHTML += `
                    <tr class="${logs.indexOf(log) % 2 === 0 ? 'bg-white' : 'bg-gray-50'} hover:bg-indigo-50 transition duration-100 cursor-pointer" data-log-id="${log.log_id}">
                        <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">${log.date}</td>
                        <td class="px-6 py-4 whitespace-nowrap">
                            <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${completionClass}">
                                ${log.is_completed ? 'Yes' : 'No'}
                            </span>
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">${valueDisplay}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-gray-500">${log.log_id}</td>
                    </tr>
                `;
            });

            tableHTML += `</tbody></table></div>`;
            historyContainer.innerHTML = tableHTML;
        }


        /**
         * Helper function to format Date object into YYYY-MM-DD string for input fields.
         */
        function formatDateInput(date) {
            const yyyy = date.getFullYear();
            const mm = String(date.getMonth() + 1).padStart(2, '0');
            const dd = String(date.getDate()).padStart(2, '0');
            return `${yyyy}-${mm}-${dd}`;
        }


        // --- EVENT LISTENERS & INITIALIZATION ---

        // 1. Form Submission Listener
        logForm.addEventListener('submit', handleLogSubmission);

        // 2. Completion Status Button Listeners (Toggle state for form submission)
        document.getElementById('btn-complete').addEventListener('click', () => {
            document.getElementById('btn-complete').dataset.status = 'true';
            document.getElementById('btn-incomplete').dataset.status = 'false'; // Ensure the other button is correctly set
        });

        document.getElementById('btn-incomplete').addEventListener('click', () => {
            document.getElementById('btn-incomplete').dataset.status = 'false';
            document.getElementById('btn-complete').dataset.status = 'true';
        });


        // 3. History Button Listener
        fetchHistoryBtn.addEventListener('click', handleFetchHistory);

        // Initialize the application when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', () => {
            setDateToToday(); // Set default date for logging form
            loadHabits();    // Load habits and initial history view
        });

    </script>
</body>
</html>
```
