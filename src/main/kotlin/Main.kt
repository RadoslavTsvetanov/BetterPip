import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.File
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.OutputStreamWriter
import java.lang.reflect.Type



class ShellSession {
    private val processBuilder = ProcessBuilder()
    private val process = processBuilder.command("bash").start()
    private val writer = OutputStreamWriter(process.outputStream)
    private val reader = BufferedReader(InputStreamReader(process.inputStream))
    private val errorReader = BufferedReader(InputStreamReader(process.errorStream))

    init {
        Runtime.getRuntime().addShutdownHook(Thread {
            writer.close()
            reader.close()
            errorReader.close()
            process.destroy()
        })
    }

    fun execute(command: String): String {
        writer.write("$command\n")
        writer.flush()

        val output = StringBuilder()
        val errorOutput = StringBuilder()

        // Read the output
        var line: String?
        while (true) {
            if (reader.ready()) {
                line = reader.readLine()
                if (line != null) {
                    output.append(line).append("\n")
                }
            } else {
                Thread.sleep(50)
                break
            }
        }

        // Read the error output
        while (true) {
            if (errorReader.ready()) {
                line = errorReader.readLine()
                if (line != null) {
                    errorOutput.append(line).append("\n")
                }
            } else {
                Thread.sleep(50)
                break
            }
        }

        return if (errorOutput.isNotEmpty()) {
            errorOutput.toString()
        } else {
            output.toString()
        }
    }

}



fun checkIfFileExists(filename: String): Boolean {
    val file = File(filename)
    return file.exists()
}

fun runShellCommand(command: String): String {
    val processBuilder = ProcessBuilder()
    processBuilder.command("sh", "-c", command)
    val output = StringBuilder()

    try {
        val process = processBuilder.start()
        val reader = BufferedReader(InputStreamReader(process.inputStream))
        val errorReader = BufferedReader(InputStreamReader(process.errorStream))

        var line: String?
        while (reader.readLine().also { line = it } != null) {
            output.append(line).append("\n")
        }

        while (errorReader.readLine().also { line = it } != null) {
            output.append(line).append("\n")
        }

        val exitCode = process.waitFor()
        output.append("Exited with code: $exitCode\n")
    } catch (e: Exception) {
        output.append("Exception: ${e.message}\n")
    }

    return output.toString()
}

data class Dependency(
    val name: String,
    val version: String
)

data class DependencyGroup(
    val dependencies: List<Dependency>
)

data class Script(
    val name: String,
    val thingToExecute: String
)

data class Configuration(
    val name: String,
    val description: String,
    val dependencies: List<DependencyGroup>,
    val scripts: List<Script>
)

class Config {
    var filename = "config.json"
        private set

    private val gson = Gson()

    fun read(): Configuration {
        val file = File(filename)
        if (file.exists()) {
            val content = file.readText()
            val type: Type = object : TypeToken<Configuration>() {}.type
            return gson.fromJson(content, type)
        } else {
            throw Error("No file with this name exists")
        }
    }

    fun write(newConfig: Configuration) {
        val file = File(filename)
        val json = gson.toJson(newConfig)
        file.writeText(json)
    }

    fun createDefaultConfig(): Configuration {
        return Configuration(
            name = "My Application",
            description = "This is a sample configuration for my application.",
            dependencies = listOf(
                DependencyGroup(
                    listOf(
                        Dependency("library1", "1.0"),
                        Dependency("library2", "2.0")
                    )
                ),
                DependencyGroup(
                    listOf(
                        Dependency("utility-library", "1.5")
                    )
                )
            ),
            scripts = listOf(
                Script("Script1", "echo 'Executing Script1'"),
                Script("Script2", "echo 'Executing Script2'")
            )
        )
    }
}

class Better_PIP_CLI : Base_cli() {
    fun install_dependency(dependency: String) {
        val venvPath = System.getenv("VIRTUAL_ENV")
        val pythonExecutable = "$venvPath/bin/python"

        when (checkIfVenvIsActive()) {
            true -> {
                runShellCommand("$pythonExecutable -m pip install $dependency")
            }
            false -> {
                println(runShellCommand("python3 -m venv .")) // Create virtual environment
                runShellCommand("$pythonExecutable -m pip install $dependency")
            }
        }
    }

    fun remove_dependency(dependency: String) {
        // Implementation goes here
    }

    fun install_dependencies() {
        // Implementation goes here
    }
}

fun checkIfVenvIsActive(): Boolean {
    val venvPath = System.getenv("VIRTUAL_ENV")
    return !venvPath.isNullOrEmpty()
}

interface CLI {
    fun list_options(): String
    fun init()
}

open class Base_cli : CLI {
    protected val config = Config()

    override fun list_options(): String {
        return "List of options not implemented yet."
    }

    override fun init() {
        if (checkIfFileExists(config.filename)) {
            println("config already exists!")
            return
        }

        val defaultConfig = config.createDefaultConfig()
        config.write(defaultConfig)
    }
}

fun main() {
    val shell = ShellSession()
    val result = shell.execute("echo >> poop.txt")
    println(result)

}
