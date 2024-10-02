package net.jotred.playershops_tfc;

import com.mojang.logging.LogUtils;
import net.jotred.playershops_tfc.common.PlayershopsTFCCreativeTabs;
import net.jotred.playershops_tfc.common.blockentities.PlayershopsTFCBlockEntities;
import net.jotred.playershops_tfc.common.blocks.PlayershopsTFCBlocks;
import net.jotred.playershops_tfc.common.items.PlayershopsTFCItems;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.config.ModConfig;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.slf4j.Logger;

// The value here should match an entry in the META-INF/mods.toml file
@Mod(PlayershopsTFC.MODID)
public class PlayershopsTFC
{
    public static final String MODID = "playershops_tfc";
    private static final Logger LOGGER = LogUtils.getLogger();

    public PlayershopsTFC()
    {
        IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();

        bus.addListener(this::commonSetup);
        
        MinecraftForge.EVENT_BUS.register(this);

        PlayershopsTFCItems.ITEMS.register(bus);
        PlayershopsTFCBlocks.BLOCKS.register(bus);
        PlayershopsTFCBlockEntities.BLOCK_ENTITIES.register(bus);
        PlayershopsTFCCreativeTabs.CREATIVE_TABS.register(bus);
    }

    private void commonSetup(final FMLCommonSetupEvent event)
    {
        // Some common setup code
        LOGGER.info("Playershops, now with TFC support, loading in...");
    }
}
